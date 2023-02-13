FROM python:3.10-slim

RUN apt-get update && apt-get -y install \
    gdal-bin \
    libgdal-dev \
    build-essential && \
  pip install --upgrade pip && \
  pip install --no-cache-dir setuptools==57.4.0 && \
  pip install --no-cache-dir GDAL==3.2.2 && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* && \
  apt-get remove -y build-essential libgdal-dev && \
  apt-get autoremove -y && \
  mkdir /app

WORKDIR /app
ADD . .

RUN pip install .

ENTRYPOINT [ "./docker-entrypoint.sh" ]
