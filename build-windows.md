Note: If you are looking for the prepared geojson data, you can download from https://front.geospatial.jp/moj-chizu-shp-download/
(You don't need to install this project)

# How to build on Windows (without WSL2)

To build this project on Windows, you need:
- Git
- Python 3
- pip 22 or over
- Anaconda
- GDAL (download from https://gdal.org/download.html )

## Install Git

1. Download the latest version of Git from https://git-scm.com/download/win

2. Install it.

3. Verify that Git is installed correctly.

```
> git --version
```

## Install Python 3

1. Download the latest version of Python 3 from https://www.python.org/downloads/

2. Install it.

3. Verify that Python is installed correctly.

```
> py --version
> py -m pip --version
```

## Install Anaconda

1. Download the latest version of Anaconda from https://www.anaconda.com/download

2. Install it.

3. Configure Anaconda for the first time:

  - In `Powershell`, run the following command:
    ```
    C:\(path to)\anaconda3\condabin\conda.bat init powershell
    ```

  - In `Command prompt`, run the following command:
    ```
    C:\(path to)\Scripts\conda init cmd.exe
    ```
  - Replace `(path to)` with the path to the Anaconda3 directory you installed.

4. Close and reopen the terminal window. The `conda` command should now work.

5. Verify that Anaconda is installed correctly by running the following command in a terminal:
```
>conda info
```

## Install GDAL for Windows

1. Run the following command in a terminal to install GDAL using conda:

```
conda install -c conda-forge gdal
```

## Install mojxml2geojson

To install mojxml2geojson, run the following command in a terminal:

```
pip install git+https://github.com/digital-go-jp/mojxml2geojson.git
```

In the installation is successful, you should be able to find the `mojxml2geojson.exe` file.


```
> mojxml2geojson.exe
usage: mojxml2geojson [-h] [-e] FILE_PATH
mojxml2geojson: error: the following arguments are required: FILE_PATH
```

## Use mojxml2geojson

To use mojxml2geojson, run the following command in a terminal:

```
mojxml2geojson.exe ./moj.xml
```

This will convert the `moj.xml` to a GeoJSON file.