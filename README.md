# mojxml2geojson

- Data converter for the National Land Register data (mojxml).
  - [What is the National Land Register data?](https://data-gov.note.jp/n/n367f1e368d22#a12a292e-4301-4cf1-979f-74f3bef09999)

- The conversion specifications are as follows.
  - Extracts and outputs only the brush polygon data and attributes necessary to maintain the Address Base Registry from the Map XML data. Reference points, boundary points, and boundary lines are not output.
  - For public coordinate information data, convert coordinate values to longitude and latitude (JGD2011). Add representative point coordinates as attributes.
  - Data in arbitrary coordinate information are not converted to coordinate values.

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
pip install git+https://github.com/digital-go-jp/mojxml2geojson.git
```

## Usage

```bash
mojxml2geojson ./moj.xml
```

### Usage with Docker

```
docker build -t mojxml2geojson .
```

Create a `data` directory and put in the files to be converted.

```
docker run --rm -v $(pwd)/data:/data mojxml2geojson /data/moj.xml 
```

### PyTest

```bash
python -m pytest -vv -p no:cacheprovide
```
