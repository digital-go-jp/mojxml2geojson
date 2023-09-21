# mojxml2geojson

- 登記所備付地図データコンバータ (mojxml).
  - [登記所備付地図データとは?](https://data-gov.note.jp/n/n367f1e368d22#440215a5-467e-4da4-8b8c-ede31710e723)

- 変換仕様は以下の通りです。
  - 地図XMLデータから、住所基台帳の管理に必要な筆ポリゴンデータと属性のみを抽出して出力します。基準点、境界点、境界線は出力しません。
  - 公開座標情報データについては、座標値を緯度経度に変換します（JGD2011）。代表点座標を属性として追加します。
  - 任意座標情報のデータは座標値に変換しません。


##注
- 変換済みのGeoJSONデータをお探しの場合、 https://front.geospatial.jp/moj-chizu-shp-download/ からダウンロードすることができます。(このプログラムをインストールする必要はありません)

## 要件

- GDAL
  - https://gdal.org/download.html
- python 3.*
- pip 22.*
- Anaconda 3.*

## インストール

- [Windowsにインストールする場合はこちら](./build-windows-ja.md)

### setup.py

```bash
pip install .
```

### GitHubからインストール

```bash
pip install git+https://github.com/digital-go-jp/mojxml2geojson.git
```

## 使用方法

```bash
mojxml2geojson ./moj.xml
```

### Dockerを使った使用方法

```
docker build -t mojxml2geojson .
```

`data` ディレクトリを作成し、変換するファイルを配置してください。

```
docker run --rm -v $(pwd)/data:/data mojxml2geojson /data/moj.xml 
```

### PyTest

```bash
python -m pytest -vv -p no:cacheprovide
```
