※ 変換済みのGeoJSONデータをお探しの場合、 https://front.geospatial.jp/moj-chizu-shp-download/ からダウンロードすることができます。(このプログラムをインストールする必要はありません)

# Windows（WSL2を使用しない）で構築する方法

このプロジェクトをWindowsで構築するには、次のものが必要です。
- Git
- Python 3
- pip 22以上
- Anaconda
- GDAL

## Gitのインストール

1. https://git-scm.com/download/winから最新のGitをダウンロードします。
  
2. インストールします。
  
3. Gitが正しくインストールされていることを確認します。

```
> git --version
```

## Python 3のインストール

1. https://www.python.org/downloads/から最新のPython 3をダウンロードします。

2. インストールします。

3. Pythonが正しくインストールされていることを確認します。


```
> py --version
> py -m pip --version
```

## Anacondaのインストール

1. https://www.anaconda.com/downloadから最新のAnacondaをダウンロードします。

2. インストールします。

3. Anacondaを初めて設定します。

  - `Powershell`の場合、次のコマンドを実行します。
    ```
    C:\(path to)\anaconda3\condabin\conda.bat init powershell
    ```

  - `コマンドプロンプト`の場合、次のコマンドを実行します。
    ```
    C:\(path to)\Scripts\conda init cmd.exe
    ```
  - `(path to)`の部分は、Anaconda3をインストールしたディレクトリへのパスに置き換えてください。

4. ターミナルウィンドウを閉じて再度開きます。`conda`コマンドが動作するはずです。

5. Anacondaが正しくインストールされていることを確認するには、ターミナルで次のコマンドを実行します。
```
>conda info
```

## Windows用のGDALのインストール

1. ターミナルで次のコマンドを実行して、condaを使用してGDALをインストールします。

```
conda install -c conda-forge gdal
```

## mojxml2geojsonのインストール

mojxml2geojsonをインストールするには、ターミナルで次のコマンドを実行します。

```
pip install git+https://github.com/digital-go-jp/mojxml2geojson.git
```

インストールが成功すると、`mojxml2geojson.exe`ファイルが見つかるはずです。

```
> mojxml2geojson.exe
usage: mojxml2geojson [-h] [-e] FILE_PATH
mojxml2geojson: error: the following arguments are required: FILE_PATH
```

## mojxml2geojsonの使い方

mojxml2geojsonを使用するには、ターミナルで次のコマンドを実行します。

```
mojxml2geojson.exe ./moj.xml
```

これにより、`moj.xml` がGeoJSONファイルに変換されます。