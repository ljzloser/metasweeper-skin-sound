# Meta-Minesweeper Skin & Sound

A single plugin for managing both game skins and sound packs. It preserves the existing `SkinManagerPlugin` identity, configuration, translations, and data directory so existing installations keep their saved choices and imported packs.

## Features

- Eight bundled skins and the `soft` sound pack.
- Import skin and sound packs from ZIP files, with path and file validation.
- Preview sound events and apply selections immediately in memory.
- Apply saved settings automatically when the plugin starts.
- Separate control authorization for `SetSkinCommand` and `SetSoundCommand`.
- English, German, Japanese, and Polish Qt translations.

The host application continues to own and apply both commands. This package uses the host-provided `plugin_sdk` and `shared_types`; it adds no runtime pip requirements.

## Install

Copy the `skin_manager/` package directory into the application's `plugins/` directory, or install the published package from the Plugin Market. Restart the plugin manager after installation. Enable the plugin and grant either or both controls in Plugin Manager's Control Authorization dialog.

The stable plugin name is `皮肤与音效`; plugin data remains under `data/plugin_data/SkinManagerPlugin/`, including the existing `config.json`, imported skins, and imported sounds.

## Development

The package directory is the repository's top-level plugin package and exports `SkinManagerPlugin` from `skin_manager/__init__.py`. Bundled resources are resolved relative to this package. Skin and sound ZIP imports are stored in the stable plugin data directory.

The `tools/` directory contains the existing skin generators. There are no third-party runtime requirements.

## 许可证

本仓库的原创插件代码采用 [0BSD 许可证](LICENSE)。第三方代码及素材遵循各自的许可证或授权条款。
