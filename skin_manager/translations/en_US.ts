<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.1" language="en_US" sourcelanguage="zh_CN">
    <context>
        <name>SkinManagerPlugin</name>
        <message>
            <location filename="../config.py" line="32" />
            <location filename="../plugin.py" line="126" />
            <source>默认皮肤</source>
            <translation>Default skin</translation>
        </message>
        <message>
            <location filename="../config.py" line="76" />
            <location filename="../config.py" line="97" />
            <source>当前皮肤</source>
            <translation>Current skin&gt;</translation>
        </message>
        <message>
            <location filename="../config.py" line="78" />
            <location filename="../config.py" line="99" />
            <source>选择后立即生效（纯内存热替换，不重启）；选「默认皮肤」即还原</source>
            <translation>Applies immediately (in-memory, no restart); choose default to restore&gt;</translation>
        </message>
        <message>
            <location filename="../config.py" line="89" />
            <source>启动时自动应用</source>
            <translation>Auto-apply on startup&gt;</translation>
        </message>
        <message>
            <location filename="../config.py" line="90" />
            <source>插件启动并连接主进程后，自动应用上次选择的皮肤</source>
            <translation>Reapply the last selected skin after the plugin connects</translation>
        </message>
        <message>
            <location filename="../config.py" line="106" />
            <source>导入皮肤包</source>
            <translation>Import skin pack&gt;</translation>
        </message>
        <message>
            <location filename="../config.py" line="108" />
            <source>导入皮肤 zip</source>
            <translation>Import skin zip&gt;</translation>
        </message>
        <message>
            <location filename="../config.py" line="109" />
            <source>选择 zip 自动解压到本插件数据目录 skins/，随后即可在下拉框选择</source>
            <translation>Extract the zip into skins/; the pack then appears in the dropdown&gt;</translation>
        </message>
        <message>
            <location filename="../plugin.py" line="69" />
            <source>在设置页选择或导入皮肤，立即应用，无需重启。</source>
            <translation>Select or import a skin in settings to apply it immediately without restarting.</translation>
        </message>
        <message>
            <location filename="../plugin.py" line="131" />
            <source>皮肤目录不存在：{name}</source>
            <translation>Skin directory does not exist: {name}</translation>
        </message>
        <message>
            <location filename="../plugin.py" line="133" />
            <source>{name}（格子 {cells}、LED {leds}、笑脸 {faces}）</source>
            <translation>{name} (cells {cells}, LEDs {leds}, faces {faces})</translation>
        </message>
        <message>
            <location filename="../plugin.py" line="138" />
            <source>主进程未响应（可能尚未连接或未授权）</source>
            <translation>Main process did not respond (possibly disconnected or unauthorized)</translation>
        </message>
        <message>
            <location filename="../plugin.py" line="142" />
            <source>应用失败：{error}</source>
            <translation>Failed to apply: {error}</translation>
        </message>
        <message>
            <location filename="../plugin.py" line="148" />
            <location filename="../plugin.py" line="211" />
            <source>已应用：{detail}</source>
            <translation>Applied: {detail}</translation>
        </message>
        <message>
            <location filename="../widgets.py" line="53" />
            <source>皮肤管理</source>
            <translation>Skin manager&gt;</translation>
        </message>
        <message>
            <location filename="../widgets.py" line="57" />
            <source>在插件列表里右键本插件 →「设置...」，从「当前皮肤」下拉框选择，选择后立即生效，无需重启。
选「默认皮肤」即可还原。</source>
            <translation>Right-click this plugin → Settings, choose a skin. Applies immediately, no restart.
Choose the default to restore.&gt;</translation>
        </message>
        <message>
            <location filename="../widgets.py" line="65" />
            <source>尚未应用皮肤</source>
            <translation>No skin applied yet&gt;</translation>
        </message>
        <message>
            <location filename="../widgets.py" line="68" />
            <source>重新应用</source>
            <translation>Reapply&gt;</translation>
        </message>
        <message>
            <location filename="../widgets.py" line="69" />
            <source>强制把当前选中的皮肤重新发送到主进程</source>
            <translation>Force-resend the selected skin to the game process&gt;</translation>
        </message>
        <message>
            <location filename="../widgets.py" line="75" />
            <source>在插件「设置...」里用「导入皮肤包」按钮安装 zip，或把资源放到插件目录 skins/&lt;名称&gt;/ 下，导入后即自动出现在下拉框里。</source>
            <translation>Use the Import skin pack button in Settings, or put resources under skins/&lt;name&gt;/. Imported packs appear in the dropdown.&gt;</translation>
        </message>
        <message>
            <location filename="../zip_import.py" line="91" />
            <source>压缩包为空</source>
            <translation>Archive is empty</translation>
        </message>
        <message>
            <location filename="../zip_import.py" line="93" />
            <source>文件数超过上限 {limit}</source>
            <translation>File count exceeds the limit of {limit}</translation>
        </message>
        <message>
            <location filename="../zip_import.py" line="106" />
            <source>压缩包包含不安全的路径或符号链接</source>
            <translation>Archive contains unsafe paths or symbolic links</translation>
        </message>
        <message>
            <location filename="../zip_import.py" line="110" />
            <source>不允许的文件类型: {path}</source>
            <translation>Disallowed file type: {path}</translation>
        </message>
        <message>
            <location filename="../zip_import.py" line="113" />
            <source>单文件过大（上限 {limit} KB）: {path}</source>
            <translation>File too large (limit {limit} KB): {path}</translation>
        </message>
        <message>
            <location filename="../zip_import.py" line="117" />
            <source>解压后总大小超过上限 {limit} MB</source>
            <translation>Uncompressed size exceeds the limit of {limit} MB</translation>
        </message>
        <message>
            <location filename="../zip_import.py" line="158" />
            <source>找不到文件: {path}</source>
            <translation>File not found: {path}</translation>
        </message>
        <message>
            <location filename="../zip_import.py" line="173" />
            <source>包名无效（不能为空、下划线开头或保留设备名）</source>
            <translation>Invalid pack name (empty, starts with an underscore, or a reserved device name)</translation>
        </message>
        <message>
            <location filename="../zip_import.py" line="211" />
            <source>压缩包内没有找到任何皮肤资源（可能需要检查目录结构）</source>
            <translation>No skin resources found in the archive. Check its directory structure.</translation>
        </message>
        <message>
            <location filename="../zip_import.py" line="235" />
            <source>写入资源包失败: {error}</source>
            <translation>Failed to write resource pack: {error}</translation>
        </message>
        <message>
            <location filename="../zip_import.py" line="262" />
            <source>导入 zip 包</source>
            <translation>Import ZIP pack</translation>
        </message>
        <message>
            <location filename="../zip_import.py" line="281" />
            <location filename="../zip_import.py" line="340" />
            <source>尚未导入</source>
            <translation>Not imported</translation>
        </message>
        <message>
            <location filename="../zip_import.py" line="297" />
            <source>选择 zip 包</source>
            <translation>Select ZIP pack</translation>
        </message>
        <message>
            <location filename="../zip_import.py" line="297" />
            <source>Zip 文件 (*.zip);;所有文件 (*)</source>
            <translation>ZIP files (*.zip);;All files (*)</translation>
        </message>
        <message>
            <location filename="../zip_import.py" line="304" />
            <location filename="../zip_import.py" line="308" />
            <source>导入失败：{error}</source>
            <translation>Import failed: {error}</translation>
        </message>
        <message>
            <location filename="../zip_import.py" line="314" />
            <location filename="../zip_import.py" line="336" />
            <source>已导入「{name}」({count} 个文件)</source>
            <translation>Imported “{name}” ({count} files)</translation>
        </message>
        <message>
            <location filename="../zip_import.py" line="329" />
            <location filename="../zip_import.py" line="338" />
            <source>已导入</source>
            <translation>Imported</translation>
        </message>
    </context>
</TS>
