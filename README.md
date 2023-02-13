# mojxml2geojson

## Requirement

- GDAL
  - https://gdal.org/download.html
- python 3.*
- pip 22.*

## Installing

### setup.py

```bash
pip install .
```

### From GitHub

```bash
pip install git+https://github.com/JDA-DM/mojxml2geojson.git
```

## Usage

```bash
mojxml2geojson ./moj.xml
```

### Usage with Docker

```
docker build -t mojxml2geojson .
```

`data` ディレクトリを作成し、変換するファイルを入れる。

```
docker run --rm -v $(pwd)/data:/data mojxml2geojson /data/moj.xml 
```

### PyTest

```bash
python -m pytest -vv -p no:cacheprovide
```
