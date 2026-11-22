"""回归测试：皮肤包导入、皮肤授权与启动时重新应用。"""
from __future__ import annotations

import pytest

from PySide6.QtWidgets import QApplication
from shared_types.commands import SetSkinCommand


@pytest.fixture(scope="module", autouse=True)
def _app():
    app = QApplication.instance() or QApplication([])
    yield app


@pytest.fixture(autouse=True)
def _isolate_plugin_data(tmp_path, monkeypatch):
    from plugin_manager import app_paths

    monkeypatch.setattr(
        app_paths, "get_plugin_data_dir", lambda _plugin: tmp_path / "SkinManagerPlugin")


def test_import_zip_end_to_end(tmp_path):
    import json
    import shutil
    import zipfile
    from skin_manager.zip_import import (
        import_zip, imported_dir, ZipImportError,
    )
    from skin_manager.config import discover_choices

    zp = tmp_path / "pack.zip"
    with zipfile.ZipFile(zp, "w") as z:
        z.writestr("my_pack/skin.json",
                   json.dumps({"name": "测试包"}, ensure_ascii=False))
        z.writestr("my_pack/cellup.svg", b"FAKE")

    root = imported_dir("skins")
    shutil.rmtree(root / "my_pack", ignore_errors=True)
    result = import_zip(zp, root)
    try:
        assert result.pack_name == "my_pack"
        assert (root / "my_pack" / "cellup.svg").is_file()
        assert any(v == "my_pack" for v, _ in discover_choices())
        assert any(v == "" for v, _ in discover_choices())
    finally:
        shutil.rmtree(root / "my_pack", ignore_errors=True)

    bad = tmp_path / "evil.zip"
    with zipfile.ZipFile(bad, "w") as z:
        z.writestr("../evil.svg", b"x")
    with pytest.raises(ZipImportError):
        import_zip(bad, root)


def test_import_zip_handles_nested_root_and_rejects_empty(tmp_path):
    """顶层多一个 README / 资源在子目录时也能定位到资源根。"""
    import json
    import shutil
    import zipfile
    from skin_manager.zip_import import import_zip, ZipImportError

    zp = tmp_path / "nested.zip"
    with zipfile.ZipFile(zp, "w") as z:
        z.writestr("outer/images/cellup.svg", b"FAKE")
        z.writestr("outer/skin.json",
                   json.dumps({"name": "嵌套包"}, ensure_ascii=False))

    root = tmp_path / "imported"
    shutil.rmtree(root / "outer", ignore_errors=True)
    result = import_zip(zp, root)
    try:
        # 资源根定位到 outer/images/，但 meta 在 outer/ 下，显示名仍应读到
        assert result.pack_name == "outer"
        assert (root / "outer" / "cellup.svg").is_file() or (
            root / "outer" / "images" / "cellup.svg").is_file()
        assert result.display == "嵌套包"
    finally:
        shutil.rmtree(root / "outer", ignore_errors=True)

    empty = tmp_path / "empty.zip"
    with zipfile.ZipFile(empty, "w") as z:
        z.writestr("readme.txt", "x")
    with pytest.raises(ZipImportError):
        import_zip(empty, root)


def test_plugin_declares_skin_control():
    from skin_manager.plugin import SkinManagerPlugin
    required = SkinManagerPlugin.plugin_info().required_controls
    assert required == [SetSkinCommand]


@pytest.mark.parametrize(
    ("skin", "skin_results", "expected_delays"),
    [
        ("", [], [1500]),
        ("classic", [True], [1500]),
        ("classic", [False, True], [1500, 2000]),
        ("classic", ["rejected", True], [1500, 2000]),
        ("classic", [False, False], [1500, 2000]),
    ],
)
def test_plugin_startup_retries_failed_skin(
        monkeypatch, skin, skin_results, expected_delays):
    from types import MethodType, SimpleNamespace
    from PySide6.QtCore import QTimer
    from skin_manager import plugin as skin_plugin

    class Signal:
        def disconnect(self, _slot):
            pass

        def connect(self, _slot, _connection):
            pass

    calls = []
    results = iter(skin_results)

    def request(cmd, timeout):
        assert isinstance(cmd, SetSkinCommand)
        calls.append(cmd)
        result = next(results)
        if result == "rejected":
            return SimpleNamespace(success=False, error="not authorized")
        return SimpleNamespace(success=True) if result else None

    instance = SimpleNamespace(
        other_info=SimpleNamespace(auto_apply=True, skin=skin),
        config_changed=Signal(), _on_config_changed=lambda *_: None,
        _refresh_choices=lambda: None,
        _roots=lambda: [], _notify=lambda _text: None, request=request,
        logger=SimpleNamespace(info=lambda *_: None, warning=lambda *_: None),
        # 模拟停用后重启时残留上一次成功的缓存。
        _applied=skin or None,
    )
    instance._apply = MethodType(skin_plugin.SkinManagerPlugin._apply, instance)
    scheduled = []
    monkeypatch.setattr(QTimer, "singleShot", lambda delay, callback:
                        scheduled.append((delay, callback)))
    monkeypatch.setattr(skin_plugin, "build_command", lambda *_: SetSkinCommand())

    skin_plugin.SkinManagerPlugin.on_initialized(instance)
    delays = []
    while scheduled:
        delay, callback = scheduled.pop(0)
        delays.append(delay)
        callback()
    assert len(calls) == len(skin_results)
    assert delays == expected_delays


def test_safe_disconnect_is_silent_when_not_connected():
    """回归：PySide6 的 disconnect 未连接时发 RuntimeWarning 而非抛异常，
    插件初始化不应再刷 'libpyside: Failed to disconnect' 告警。"""
    import warnings
    from PySide6.QtCore import QObject, Signal
    from skin_manager.plugin import _safe_disconnect

    class _Emitter(QObject):
        sig = Signal(str)

    emitter = _Emitter()

    def slot(_x):
        pass

    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        _safe_disconnect(emitter.sig, slot)
        assert not [w for w in caught
                    if "Failed to disconnect" in str(w.message)]

    # 已连接时应真正断开，且同样无告警
    emitter.sig.connect(slot)
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        _safe_disconnect(emitter.sig, slot)
        assert not [w for w in caught
                    if "Failed to disconnect" in str(w.message)]
