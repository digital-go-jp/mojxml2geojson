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

### From Github

```bash
pip install git+https://github.com/JDA-DM/mojxml2geojson.git
```

## Usege

### Single File

```bash
mojxml2geojson ./moj.xml
```

### Multiple files

```bash
cd [target directory]
ls -1 *.xml|xargs -I{} mojxml2geojson ./{}
```

**Parallel Processing**

```bash
ls -1 *.xml|xargs -P100 -I{} mojxml2geojson ./{}
```

### PyTest

```bash
python -m pytest -vv -p no:cacheprovide
```
