<!-- https://hadoop.apache.org/docs/r3.4.1/hadoop-project-dist/hadoop-common/ClusterSetup.html -->

# Hadoopクラスタのセットアップ

- 目的
- 前提条件
- インストール
- 非セキュアモードでのHadoopの設定
    - Hadoopデーモンの環境設定
    - Hadoopデーモンの設定
- NodeManagersの健全性の監視
- スレーブファイル
- Hadoop ラックの認識
- ロギング
- Hadoopクラスタの操作
    - Hadoopの起動
    - Hadoopのシャットダウン
- ウェブインターフェース

## 目的

このドキュメントでは、数ノードから数千ノードの超大規模クラスタまで、Hadoopクラスタのインストールと設定方法について説明します。Hadoopで遊ぶには、まず1台のマシンにインストールしてみましょう（シングルノードのセットアップを参照[1]）。

[1] https://hadoop.apache.org/docs/r3.4.1/hadoop-project-dist/hadoop-common/SingleCluster.html

このドキュメントでは、High Availabilityのような高度なトピックはカバーしていません。

重要: すべてのプロダクションHadoopクラスタは、Kerberosを使用して呼び出し元を認証し、HDFSデータへの安全なアクセスと計算サービス（YARNなど）へのアクセスを制限します。

本番クラスターを立ち上げる際には、デプロイの重要な部分として組織のKerberosインフラへの接続を含める必要があります。

クラスタをセキュアにする方法の詳細については、セキュリティ[2]を参照してください。
[2] https://hadoop.apache.org/docs/r3.4.1/hadoop-project-dist/hadoop-common/SecureMode.html

## 前提条件

Javaをインストールする。既知の良いバージョンについてはHadoop Wiki[3]を参照のこと。
ApacheのミラーからHadoopの安定版をダウンロードする。

[3] https://cwiki.apache.org/confluence/display/HADOOP/Hadoop+Java+Versions

## インストール

Hadoopクラスタのインストールでは通常、クラスタ内のすべてのマシンにソフトウェアを解凍するか、オペレーティング・システムに適したパッケージング・システムを介してインストールする。ハードウェアを機能ごとに分割することが重要です。

通常、クラスタ内の1台のマシンがNameNodeとして指定され、もう1台のマシンがResourceManagerとして排他的に指定されます。これらがマスターだ。その他のサービス（Web App Proxy ServerやMapReduce Job History Serverなど）は、負荷に応じて専用のハードウェアか共有インフラで実行するのが一般的です．

クラスタ内の残りのマシンは、DataNodeとNodeManagerの両方の役割を果たします。これがワーカーです。

## 非セキュアモードでのHadoopの設定

HadoopのJavaコンフィギュレーションは、2種類の重要なコンフィギュレーションファイルによって駆動されます:

- 読み取り専用のデフォルト設定 `core-default.xml`、`hdfs-default.xml`、`yarn-default.xml`、`mapred-default.xml`
- サイト固有の設定 `etc/hadoop/core-site.xml`、`etc/hadoop/hdfs-site.xml`、`etc/hadoop/yarn-site.xml`、`etc/hadoop/mapred-site.xml`

**読取り専用用のデフォルト設定**
|ファイル名|役割|
|----|----|
|core-default.xml||
|hdfs-default.xml||
|yarn-default.xml||
|mapred-default.xml||

**サイト固有の設定**
|ファイル名|役割|
|----|----|
|etc/hadoop/core-site.xml||
|etc/hadoop/hdfs-site.xml||
|etc/hadoop/yarn-site.xml||
|etc/hadoop/mapred-site.xml||

さらに、`etc/hadoop/hadoop-env.sh`と`etc/hadoop/yarn-env.sh`でサイト固有の値を設定することで、ディストリビューションのbin/ディレクトリにあるHadoopスクリプトを制御できる。

Hadoopクラスタを構成するには、Hadoopデーモンの構成パラメータだけでなく、Hadoopデーモンが実行される環境を構成する必要があります。

HDFSデーモンはNameNode、SecondaryNameNode、DataNodeである。YARNデーモンはResourceManager、NodeManager、WebAppProxyである。MapReduceを使用する場合は、MapReduceジョブ履歴サーバーも実行される。大規模なインストールでは、これらは通常別々のホストで実行される。

### Hadoopデーモンの環境設定

管理者は、`etc/hadoop/hadoop-env.sh`、およびオプションで`etc/hadoop/mapred-env.sh`と`etc/hadoop/yarn-env.sh`スクリプトを使用して、Hadoopデーモンのプロセス環境をサイトごとにカスタマイズする必要があります。

少なくとも、各リモート・ノードで**`JAVA_HOME`**が正しく定義されるように指定しなければならない。

管理者は、以下の表に示す構成オプションを使用して、個々のデーモンを構成できます:

**HDFSデーモン**

|Daemon|環境変数|役割|
|----|----|----|
|NameNode|HDFS_NAMENODE_OPTS||
|DataNode|HDFS_DATANODE_OPTS||
|Secondary NameNode|HDFS_SECONDARYNAMENODE_OPTS||

**YARNデーモン**

|Daemon|環境変数|役割|
|----|----|----|
|ResourceManager|YARN_RESOURCEMANAGER_OPTS||
|NodeManager|YARN_NODEMANAGER_OPTS||
|WebAppProxy|YARN_PROXYSERVER_OPTS||

**MapReduceサーバ**

|Daemon|環境変数|役割|
|----|----|----|
|Map Reduce Job History Server|MAPRED_HISTORYSERVER_OPTS||

例えば、Namenode が parallelGC と 4GB の Java ヒープを使うように設定するには、hadoop-env.sh に以下のステートメントを追加します:

```bash
export HDFS_NAMENODE_OPTS="-XX:+UseParallelGC -Xmx4g"    # ParallelGC（パラレルGC） は、その中でも 複数のCPUを使って効率よく掃除する方法
```

他の例については `etc/hadoop/hadoop-env.sh` を参照してください。

その他にカスタマイズできる便利な設定パラメータは以下のとおりです：

- HADOOP_PID_DIR - デーモンのプロセス ID ファイルが格納されるディレクトリ。
- HADOOP_LOG_DIR - デーモンのログ・ファイルが格納されるディレクトリ。ログファイルが存在しない場合は自動的に作成されます。
- HADOOP_HEAPSIZE_MAX - Java ヒープ・サイズに使用するメモリの最大量。JVMによってサポートされるユニットもここでサポートされます。
    - 単位がない場合は、メガバイト単位とみなされます。
    - デフォルトでは、HadoopはJVMに使用量を決定させます。
    - この値は、上記の適切な_OPTS変数を使用して、デーモンごとにオーバーライドできます。
    ```bash
    # 例えば、
    HADOOP_HEAPSIZE_MAX=1g
    # と
    HADOOP_NAMENODE_OPTS="-Xmx5g "
    # を設定すると、NameNodeは5GBヒープで構成されます。
    ```

ほとんどの場合、HADOOP_PID_DIR と HADOOP_LOG_DIR ディレクトリは、hadoop デーモンを実行するユーザだけが書き込めるように指定する必要があります。そうしないとシンボリックリンク攻撃の可能性があります。

システム全体のシェル環境設定で`HADOOP_HOME`を設定するのも伝統的な方法です。例えば、`/etc/profile.d` 内に簡単なスクリプトを記述します:

```bash
HADOOP_HOME=/path/to/hadoop
export HADOOP_HOME
```

### Hadoopデーモンの設定

このセクションでは、与えられたコンフィギュレーション・ファイルで指定されるべき重要なパラメーターについて説明します．

#### `etc/hadoop/core-site.xml`

|パラメタ|値|備考|
|----|----|----|
|fs.defaultFS|<NameNode URI>|hdfs://host:port/|
|io.file.buffer.size|131072|SequenceFilesで使用される読み書きバッファのサイズ|

#### `etc/hadoop/hdfs-site.xml`

NameNodeに対する設定項目

|パラメタ|値|備考|
|----|----|----|
|dfs.namenode.name.dir|NameNodeが処理ログを保存する場所を指定する設定|これがカンマで区切られたディレクトリのリストすべてにテーブルが複製される|
|dfs.hosts/dfs.hosts.exclude|許可/除外されたデータノードのリスト|必要に応じて、これらのファイルを使用して、許可されるデータノードのリストを制御する|
|dfs.blocksize|268435456|大規模ファイルシステムのためにHDFSブロックサイズを256MBに指定している|
|dfs.namenode.handler.count|100|NameNodeのハンドラ数|

DataNodeに対する設定項目

|パラメタ|値|備考|
|----|----|----|
|dfs.datanode.data.dir|DataNodeがブロックを格納するローカルファイルシステム上のパスをカンマ区切りで列挙したもの|通常異なるディスクのマウントパスがカンマ区切りで列挙され，その全てにデータブロックが分散される|

#### `etc/hadoop/yarn-site.xml`

ResourceManagerとNodeManagerに対する共通の設定項目

|パラメタ|値|備考|
|----|----|----|
|yarn.acl.enable|true/false||
|yarn.admin.acl|Admin ACL||
|yarn.log-aggregation-enable|false||

ResourceManagerに対する設定項目

|パラメタ|値|備考|
|----|----|----|
|yarn.resourcemanager.address|クライアントがジョブを送信するための ResourceManager のホスト:ポート。|ホスト:ポート この値を設定すると、`yarn.resourcemanager.hostname` で設定されたホスト名を上書きする。|
|yarn.resourcemanager.scheduler.address|ApplicationMaster がリソースを取得するために Scheduler と通信する ResourceManager のホスト:ポート。|ホスト:ポート この値を設定すると、`yarn.resourcemanager.hostname` で設定されたホスト名を上書きする。|
|yarn.resourcemanager.resource-tracker.address|NodeManager が接続するための ResourceManager のホスト:ポート。|ホスト:ポート この値を設定すると、`yarn.resourcemanager.hostname` で設定されたホスト名を上書きする。|
|yarn.resourcemanager.admin.address|管理コマンドを実行するための ResourceManager のホスト:ポート。|ホスト:ポート この値を設定すると、`yarn.resourcemanager.hostname` で設定されたホスト名を上書きする。|
|yarn.resourcemanager.webapp.address|ResourceManager の Web UI のホスト:ポート。|ホスト:ポート この値を設定すると、`yarn.resourcemanager.hostname` で設定されたホスト名を上書きする。|
|yarn.resourcemanager.hostname|ResourceManager のホスト名。|ホスト `yarn.resourcemanager*address` のすべての設定の代わりに、単一のホスト名を指定できる。これにより、ResourceManager の各コンポーネントにデフォルトのポートが適用される。|
|yarn.resourcemanager.scheduler.class|ResourceManager のスケジューラクラス。|推奨: `CapacityScheduler` または `FairScheduler`。`FifoScheduler` も使用可能。完全修飾クラス名を使用すること（例: `org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.FairScheduler`）。|
|yarn.scheduler.minimum-allocation-mb|ResourceManager で各コンテナ要求に割り当てるメモリの最小値。|MB単位|
|yarn.scheduler.maximum-allocation-mb|ResourceManager で各コンテナ要求に割り当てるメモリの最大値。|MB単位|
|yarn.resourcemanager.nodes.include-path|許可された NodeManager のリスト。|必要に応じて、これらのファイルを使用して許可する NodeManager のリストを制御する。|
|yarn.resourcemanager.nodes.exclude-path|許可された NodeManager のリスト。|必要に応じて、これらのファイルを使用して許可しない NodeManager のリストを制御する。|


NodeManagerに対する設定項目

|パラメタ|値|備考|
|----|----|----|









