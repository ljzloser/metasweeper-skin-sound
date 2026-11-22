"""皮肤管理插件的状态面板。"""
from __future__ import annotations

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget,
)

from utils.plugin_i18n import PluginTranslate
from utils.translated_widgets import TranslatedLabel as QLabel, TranslatedPushButton as QPushButton

_translate = PluginTranslate("SkinManagerPlugin")

class SkinManagerWidget(QWidget):
    """显示当前皮肤的应用状态。"""

    apply_requested = Signal()

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(8)

        title = QLabel(_translate("SkinManagerPlugin", "皮肤管理"))
        title.setStyleSheet("font-size: 15pt; font-weight: bold;")
        layout.addWidget(title)

        tip = QLabel(_translate(
            "SkinManagerPlugin",
            "在插件列表里右键本插件 →「设置...」，从「当前皮肤」下拉框选择，"
            "选择后立即生效，无需重启。\n选「默认皮肤」即可还原。"))
        tip.setWordWrap(True)
        layout.addWidget(tip)

        bar = QHBoxLayout()
        self._status = QLabel(_translate("SkinManagerPlugin", "尚未应用皮肤"))
        self._status.setWordWrap(True)
        bar.addWidget(self._status, 1)
        reapply = QPushButton(_translate("SkinManagerPlugin", "重新应用"))
        reapply.setToolTip(_translate(
            "SkinManagerPlugin", "强制把当前选中的皮肤重新发送到主进程"))
        reapply.clicked.connect(self.apply_requested.emit)
        bar.addWidget(reapply)
        layout.addLayout(bar)

        hint = QLabel(_translate(
            "SkinManagerPlugin",
            "在插件「设置...」里用「导入皮肤包」按钮安装 zip，或把资源放到"
            "插件目录 skins/<名称>/ 下，导入后即自动出现在下拉框里。"))
        hint.setWordWrap(True)
        hint.setStyleSheet("color: gray; font-size: 11px;")
        layout.addWidget(hint)

        layout.addStretch(1)

    def set_status(self, text: str) -> None:
        self._status.setText(text)
