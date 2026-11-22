"""
皮肤管理插件 - 配置定义（自动注册皮肤为下拉框选项）。

参考 clipboard_replay/config.py 的做法：模块导入时扫描皮肤目录，
把每个皮肤自动注册成 ChoiceConfig 的一个选项，插件自己不需要写任何
界面代码，设置对话框会依据配置类型自动生成 QComboBox。

想加皮肤：在 skins/ 下新建一个目录、放好图片即可，下次启动自动出现在
下拉框里，无需修改任何 Python 代码。
"""
from __future__ import annotations

from pathlib import Path

from plugin_sdk import OtherInfoBase, BoolConfig, ChoiceConfig

from .skins import list_skins
from .zip_import import ZipImportConfig, imported_dir
from utils.plugin_i18n import PluginTranslate

_translate = PluginTranslate("SkinManagerPlugin")

# 插件自带皮肤库（源码/打包后都随插件目录一起分发）
BUILTIN_SKINS_DIR = Path(__file__).resolve().parent / "skins"

# "默认皮肤" 固定占一个选项（运行时按当前语言取词）
_DEFAULT_CHOICE = ("", _translate("SkinManagerPlugin", "默认皮肤"))


def discover_choices() -> list[tuple[str, str]]:
    """扫描皮肤目录，返回 ChoiceConfig 选项列表 [(目录名, 显示名), ...]。

    扫描顺序：自带 skins/ → 插件数据目录 skins/（zip 导入落地处）。
    同名以先扫描到的为准。
    """
    choices: dict[str, str] = dict(list_skins(BUILTIN_SKINS_DIR))
    for name, display in list_skins(imported_dir("skins")):
        choices.setdefault(name, display)
    items = [(name, choices[name]) for name in sorted(choices)]
    return [_DEFAULT_CHOICE, *items]


class SkinManagerConfig(OtherInfoBase):
    """皮肤管理配置"""

    auto_apply = BoolConfig(
        default=True,
        label=_translate("SkinManagerPlugin", "启动时自动应用"),
        description=_translate(
            "SkinManagerPlugin", "插件启动并连接主进程后，自动应用上次选择的皮肤"),
    )

    # ── 皮肤 ──
    skin = ChoiceConfig(
        default="",
        label=_translate("SkinManagerPlugin", "当前皮肤"),
        choices=discover_choices(),
        description=_translate(
            "SkinManagerPlugin",
            "选择后立即生效（纯内存热替换，不重启）；选「默认皮肤」即还原"),
    )

    skin_zip = ZipImportConfig(
        default="",
        label=_translate("SkinManagerPlugin", "导入皮肤包"),
        target_subdir="skins",
        button_text=_translate("SkinManagerPlugin", "导入皮肤 zip"),
        description=_translate(
            "SkinManagerPlugin",
            "选择 zip 自动解压到本插件数据目录 skins/，随后即可在下拉框选择"),
    )


def register_choices(choices: list[tuple[str, str]]) -> None:
    field = SkinManagerConfig.skin
    SkinManagerConfig.skin = ChoiceConfig(
        default=field.default, label=field.label,
        choices=choices, description=field.description,
    )
