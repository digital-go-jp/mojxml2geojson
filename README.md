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

### PyTest

```bash
python -m pytest -vv -p no:cacheprovide
```
