# Publishing

This repository follows the Meta-Minesweeper Plugin Market convention. The repository name is `metasweeper-skin-sound`; GitHub discovery uses the `metasweeper-plugin` topic, and Gitee discovery requires the `metasweeper-` name prefix.

## Release a version

1. Ensure the repository root contains the single installable package directory `skin_manager/` with its `__init__.py`, resources, and translations. Keep `requirements.txt` empty unless a future release adds a genuine runtime dependency.
2. Update `skin_manager/plugin.py`'s `PluginInfo.version` and this repository's release notes together.
3. Push the repository to a public GitHub or Gitee repository and add the `metasweeper-plugin` GitHub topic when publishing there.
4. Create and push a version tag named `metasweeper-v<version>` (for example `metasweeper-v1.1.0`). The market downloads the source archive for the tagged commit and installs the root package directory.
5. For a Gitee mirror, retain the same repository name and tag so the market recognizes it as the same plugin identity.

The plugin market index is maintained by the application project; plugin publishers do not need to submit an index pull request. Release tags are discovered from the public repository.

## Compatibility

Keep the plugin package directory named `skin_manager`, the PluginInfo name `皮肤与音效`, and the class-based data directory identity `SkinManagerPlugin`. These identify the package, persisted configuration/state, and existing user data. The host application owns `SetSkinCommand` and `SetSoundCommand` processing; the plugin declares and sends those host controls. Keep the bundled assets and all four translation catalogs in each source release.
