"""皮肤管理插件：运行时热替换主窗口图片资源（纯内存，不重启）。

皮肤选择由 config.py 自动注册成设置页里的下拉框（ChoiceConfig），
插件本身只负责把选中皮肤的图片字节通过 SetSkinCommand 发给主进程。
"""
from __future__ import annotations

import warnings
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget

from plugin_sdk import BasePlugin, PluginInfo, WindowMode
from shared_types.commands import SetSkinCommand

from .config import (
    BUILTIN_SKINS_DIR, SkinManagerConfig, discover_choices, register_choices,
)
from .skins import build_command
from .zip_import import imported_dir
from .widgets import SkinManagerWidget
from utils.plugin_i18n import PluginTranslate

_translate = PluginTranslate("SkinManagerPlugin")


def _safe_disconnect(signal, slot) -> None:
    """断开信号连接，且容忍「本来就没连上」。

    PySide6 的 `Signal.disconnect()` 在连接不存在时**不抛异常**，而是发出
    `RuntimeWarning: libpyside: Failed to disconnect ...`，因此
    `try/except (RuntimeError, TypeError)` 抓不住，会在每次插件初始化时
    刷一条告警。这里把该警告就地忽略（仅限这一句调用），并用
    try/except 兜住真正抛异常的其他绑定类型。
    """
    with warnings.catch_warnings():
        warnings.filterwarnings(
            "ignore", message=".*Failed to disconnect.*",
            category=RuntimeWarning)
        try:
            signal.disconnect(slot)
        except (RuntimeError, TypeError):
            pass


class SkinManagerPlugin(BasePlugin[SkinManagerConfig]):
    """把皮肤图片字节发给主进程，主进程只改内存缓存。"""

    def __init__(self, info: PluginInfo):
        super().__init__(info)
        # 缓存上一次成功应用的皮肤名，避免重复发送
        self._applied: str | None = None

    @classmethod
    def plugin_info(cls) -> PluginInfo:
        return PluginInfo(
            # name 是配置目录、日志、状态键与授权记录的稳定标识，不随语言变化
            name="皮肤与音效",
            display_name=_translate("SkinManagerPlugin", "皮肤管理"),
            version="1.2.0",
            description=_translate("SkinManagerPlugin",
                "在设置页选择或导入皮肤，立即应用，无需重启。"
            ),
            icon=QIcon(str(Path(__file__).resolve().with_name("icon.svg"))),
            # 默认不自动开启界面；只在启动时读取，不与窗口生命周期联动。
            show_window=False,
            window_mode=WindowMode.TAB,
            other_info=SkinManagerConfig,
            required_controls=[SetSkinCommand],
        )

    def _setup_subscriptions(self) -> None:
        # 本插件只发指令，不订阅游戏事件
        pass

    def _create_widget(self) -> QWidget:
        widget = SkinManagerWidget()
        widget.apply_requested.connect(
            self._on_apply_requested, Qt.ConnectionType.QueuedConnection)
        return widget

    # ── 皮肤库根目录（自带 + zip 导入落地目录）────────────────────
    def _roots(self) -> list[Path]:
        return [BUILTIN_SKINS_DIR, imported_dir("skins")]

    def _refresh_choices(self) -> None:
        """重新扫描皮肤目录并刷新配置类上的 ChoiceConfig 选项。"""
        choices = discover_choices()
        register_choices(choices)
        # 已实例化的配置对象持有自己的 _fields，需同步替换
        if self.other_info is not None:
            fields = self.other_info._fields
            if "skin" in fields:
                fields["skin"] = getattr(SkinManagerConfig, "skin")
        if self._applied is not None and self._applied not in dict(choices):
            # 已应用的皮肤包被删除/改名：清缓存的同时必须让主进程还原，
            # 否则插件认为「未应用」，主窗口却仍显示已消失的皮肤。
            self._applied = None
            self._apply("", force=True)
        # 配置值可能仍指向已失效的包名，同步修正回默认，避免下次 auto_apply
        # 用一个不存在的名字反复发请求。
        current = str(self.other_info.skin or "") if self.other_info else ""
        if current and current not in dict(choices):
            self.other_info.skin = ""

    # ── 应用 / 还原 ──────────────────────────────────────────────
    def _apply(self, skin_name: str, force: bool = False) -> bool:
        if not force and skin_name == self._applied:
            return True
        roots = self._roots()
        if not skin_name:
            cmd = SetSkinCommand(reset=True)
            detail = _translate("SkinManagerPlugin", "默认皮肤")
        else:
            cmd = build_command(roots, skin_name)
            if cmd.reset:
                self.logger.warning(f"皮肤目录不存在: {skin_name}")
                self._notify(_translate("SkinManagerPlugin", "皮肤目录不存在：{name}").format(name=skin_name))
                return False
            detail = _translate("SkinManagerPlugin", "{name}（格子 {cells}、LED {leds}、笑脸 {faces}）").format(
                name=skin_name, cells=len(cmd.cells), leds=len(cmd.leds), faces=len(cmd.faces))

        resp = self.request(cmd, timeout=10.0)
        if resp is None:
            self._notify(_translate("SkinManagerPlugin", "主进程未响应（可能尚未连接或未授权）"))
            self.logger.warning("SetSkinCommand 无响应，请检查连接与控制授权")
            return False
        if not resp.success:
            self._notify(_translate("SkinManagerPlugin", "应用失败：{error}").format(error=resp.error))
            self.logger.warning(f"SetSkinCommand 被拒绝: {resp.error}")
            return False

        self._applied = skin_name
        self.logger.info(f"已应用皮肤: {detail}")
        self._notify(_translate("SkinManagerPlugin", "已应用：{detail}").format(detail=detail))
        return True

    def _notify(self, text: str) -> None:
        # 在 GUI 执行时读取当前窗口，关闭期间自动跳过通知。
        self.run_on_widget(
            lambda widget, message: widget.set_status(message), text)

    def _on_apply_requested(self) -> None:
        """界面上「重新应用」按钮：强制重发一次当前皮肤。"""
        self._apply(str(self.other_info.skin or ""), force=True)

    def on_initialized(self) -> None:
        _safe_disconnect(self.config_changed, self._on_config_changed)
        self.config_changed.connect(
            self._on_config_changed, Qt.ConnectionType.QueuedConnection)
        self._refresh_choices()
        if self.other_info.auto_apply:
            from PySide6.QtCore import QTimer

            def apply_saved_skin(retry: bool) -> None:
                skin = str(self.other_info.skin or "")
                if skin and not self._apply(skin, force=True) and retry:
                    QTimer.singleShot(2000, lambda: apply_saved_skin(False))

            QTimer.singleShot(1500, lambda: apply_saved_skin(True))

    def _on_config_changed(self, name: str, value) -> None:
        if name == "skin_zip":
            self._refresh_choices()
        elif name == "skin":
            self._apply(str(value or ""))

    def on_shutdown(self) -> None:
        _safe_disconnect(self.config_changed, self._on_config_changed)
        try:
            self.request(SetSkinCommand(reset=True), timeout=2.0)
        except Exception:
            pass
