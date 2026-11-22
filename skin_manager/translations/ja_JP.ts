<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.1" language="ja_JP" sourcelanguage="zh_CN">
    <context>
        <name>SkinManagerPlugin</name>
        <message>
            <location filename="../config.py" line="32" />
            <location filename="../plugin.py" line="126" />
            <source>默认皮肤</source>
            <translation>既定のスキン</translation>
        </message>
        <message>
            <location filename="../config.py" line="76" />
            <location filename="../config.py" line="97" />
            <source>当前皮肤</source>
            <translation>現在のスキン&gt;</translation>
        </message>
        <message>
            <location filename="../config.py" line="78" />
            <location filename="../config.py" line="99" />
            <source>选择后立即生效（纯内存热替换，不重启）；选「默认皮肤」即还原</source>
            <translation>即時反映（メモリ内・再起動不要）。既定を選ぶと元に戻ります&gt;</translation>
        </message>
        <message>
            <location filename="../config.py" line="89" />
            <source>启动时自动应用</source>
            <translation>起動時に自動適用&gt;</translation>
        </message>
        <message>
            <location filename="../config.py" line="90" />
            <source>插件启动并连接主进程后，自动应用上次选择的皮肤</source>
            <translation>接続後に前回選択したスキンを適用します</translation>
        </message>
        <message>
            <location filename="../config.py" line="106" />
            <source>导入皮肤包</source>
            <translation>スキンパックをインポート&gt;</translation>
        </message>
        <message>
            <location filename="../config.py" line="108" />
            <source>导入皮肤 zip</source>
            <translation>スキン zip をインポート&gt;</translation>
        </message>
        <message>
            <location filename="../config.py" line="109" />
            <source>选择 zip 自动解压到本插件数据目录 skins/，随后即可在下拉框选择</source>
            <translation>zip を skins/ に展開後、ドロップダウンに表示されます&gt;</translation>
        </message>
        <message>
            <location filename="../plugin.py" line="69" />
            <source>在设置页选择或导入皮肤，立即应用，无需重启。</source>
            <translation>設定でスキンを選択またはインポートすると、再起動せずにすぐ適用されます。</translation>
        </message>
        <message>
            <location filename="../plugin.py" line="131" />
            <source>皮肤目录不存在：{name}</source>
            <translation>スキンのディレクトリがありません: {name}</translation>
        </message>
        <message>
            <location filename="../plugin.py" line="133" />
            <source>{name}（格子 {cells}、LED {leds}、笑脸 {faces}）</source>
            <translation>{name}（マス {cells}、LED {leds}、顔 {faces}）</translation>
        </message>
        <message>
            <location filename="../plugin.py" line="138" />
            <source>主进程未响应（可能尚未连接或未授权）</source>
            <translation>メインプロセスが応答しません（未接続または未許可の可能性があります）</translation>
        </message>
        <message>
            <location filename="../plugin.py" line="142" />
            <source>应用失败：{error}</source>
            <translation>適用に失敗: {error}</translation>
        </message>
        <message>
            <location filename="../plugin.py" line="148" />
            <location filename="../plugin.py" line="211" />
            <source>已应用：{detail}</source>
            <translation>適用済み: {detail}</translation>
        </message>
        <message>
            <location filename="../widgets.py" line="53" />
            <source>皮肤管理</source>
            <translation>スキン管理&gt;</translation>
        </message>
        <message>
            <location filename="../widgets.py" line="57" />
            <source>在插件列表里右键本插件 →「设置...」，从「当前皮肤」下拉框选择，选择后立即生效，无需重启。
选「默认皮肤」即可还原。</source>
            <translation>プラグイン一覧で右クリック →「設定」からスキンを選択。即時反映、再起動不要。
既定を選ぶと元に戻ります。&gt;</translation>
        </message>
        <message>
            <location filename="../widgets.py" line="65" />
            <source>尚未应用皮肤</source>
            <translation>スキンは未適用です&gt;</translation>
        </message>
        <message>
            <location filename="../widgets.py" line="68" />
            <source>重新应用</source>
            <translation>再適用&gt;</translation>
        </message>
        <message>
            <location filename="../widgets.py" line="69" />
            <source>强制把当前选中的皮肤重新发送到主进程</source>
            <translation>選択中のスキンを主プロセスへ強制再送信&gt;</translation>
        </message>
        <message>
            <location filename="../widgets.py" line="75" />
            <source>在插件「设置...」里用「导入皮肤包」按钮安装 zip，或把资源放到插件目录 skins/&lt;名称&gt;/ 下，导入后即自动出现在下拉框里。</source>
            <translation>「設定」の「スキンパックをインポート」、または skins/&lt;名前&gt;/ に配置するとドロップダウンに表示されます。&gt;</translation>
        </message>
        <message>
            <location filename="../zip_import.py" line="91" />
            <source>压缩包为空</source>
            <translation>アーカイブが空です</translation>
        </message>
        <message>
            <location filename="../zip_import.py" line="93" />
            <source>文件数超过上限 {limit}</source>
            <translation>ファイル数が上限の{limit}を超えています</translation>
        </message>
        <message>
            <location filename="../zip_import.py" line="106" />
            <source>压缩包包含不安全的路径或符号链接</source>
            <translation>アーカイブに安全でないパスまたはシンボリックリンクがあります</translation>
        </message>
        <message>
            <location filename="../zip_import.py" line="110" />
            <source>不允许的文件类型: {path}</source>
            <translation>許可されていないファイル形式: {path}</translation>
        </message>
        <message>
            <location filename="../zip_import.py" line="113" />
            <source>单文件过大（上限 {limit} KB）: {path}</source>
            <translation>ファイルが大きすぎます（上限{limit} KB）: {path}</translation>
        </message>
        <message>
            <location filename="../zip_import.py" line="117" />
            <source>解压后总大小超过上限 {limit} MB</source>
            <translation>展開後の合計サイズが上限の{limit} MBを超えています</translation>
        </message>
        <message>
            <location filename="../zip_import.py" line="158" />
            <source>找不到文件: {path}</source>
            <translation>ファイルが見つかりません: {path}</translation>
        </message>
        <message>
            <location filename="../zip_import.py" line="173" />
            <source>包名无效（不能为空、下划线开头或保留设备名）</source>
            <translation>無効なパック名です（空、アンダースコアで開始、または予約デバイス名）</translation>
        </message>
        <message>
            <location filename="../zip_import.py" line="211" />
            <source>压缩包内没有找到任何皮肤资源（可能需要检查目录结构）</source>
            <translation>アーカイブ内にスキンリソースがありません。ディレクトリ構造を確認してください。</translation>
        </message>
        <message>
            <location filename="../zip_import.py" line="235" />
            <source>写入资源包失败: {error}</source>
            <translation>リソースパックの書き込みに失敗: {error}</translation>
        </message>
        <message>
            <location filename="../zip_import.py" line="262" />
            <source>导入 zip 包</source>
            <translation>ZIPパックをインポート</translation>
        </message>
        <message>
            <location filename="../zip_import.py" line="281" />
            <location filename="../zip_import.py" line="340" />
            <source>尚未导入</source>
            <translation>未インポート</translation>
        </message>
        <message>
            <location filename="../zip_import.py" line="297" />
            <source>选择 zip 包</source>
            <translation>ZIPパックを選択</translation>
        </message>
        <message>
            <location filename="../zip_import.py" line="297" />
            <source>Zip 文件 (*.zip);;所有文件 (*)</source>
            <translation>ZIPファイル (*.zip);;すべてのファイル (*)</translation>
        </message>
        <message>
            <location filename="../zip_import.py" line="304" />
            <location filename="../zip_import.py" line="308" />
            <source>导入失败：{error}</source>
            <translation>インポートに失敗: {error}</translation>
        </message>
        <message>
            <location filename="../zip_import.py" line="314" />
            <location filename="../zip_import.py" line="336" />
            <source>已导入「{name}」({count} 个文件)</source>
            <translation>「{name}」をインポートしました（{count}ファイル）</translation>
        </message>
        <message>
            <location filename="../zip_import.py" line="329" />
            <location filename="../zip_import.py" line="338" />
            <source>已导入</source>
            <translation>インポート済み</translation>
        </message>
    </context>
</TS>
