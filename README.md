# Meta-Minesweeper Skins

A single plugin for managing game skins. It preserves the existing `SkinManagerPlugin` identity, configuration, translations, and data directory so existing installations keep their saved choices and imported packs.

## Features

- Eight bundled skins.
- Import skin packs from ZIP files, with path and file validation.
- Apply skins immediately in memory.
- Apply saved settings automatically when the plugin starts.
- Control authorization for `SetSkinCommand`.
- English, German, Japanese, and Polish Qt translations.

The host application continues to own and apply `SetSkinCommand`. This package uses the host-provided `plugin_sdk` and `shared_types`; it adds no runtime pip requirements.

## Install

Copy the `skin_manager/` package directory into the application's `plugins/` directory, or install the published package from the Plugin Market. Restart the plugin manager after installation. Enable the plugin and grant the skin control in Plugin Manager's Control Authorization dialog.

The stable plugin name is `皮肤与音效`; plugin data remains under `data/plugin_data/SkinManagerPlugin/`, including the existing `config.json` and imported skins.

## 1.2.0

- The plugin is now displayed as Skin Manager. Sound packs, sound settings, and sound previews have been removed.
- Existing skin selections, imported skins, and plugin identity are preserved.

## Development

The package directory is the repository's top-level plugin package and exports `SkinManagerPlugin` from `skin_manager/__init__.py`. Bundled resources are resolved relative to this package. Skin ZIP imports are stored in the stable plugin data directory.

The `tools/` directory contains the existing skin generators. There are no third-party runtime requirements.

## 许可证

本仓库的原创插件代码采用 [MIT 许可证](LICENSE)。第三方代码及素材遵循各自的许可证或授权条款。
