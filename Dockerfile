FROM ubuntu:latest

RUN apt-get update && apt-get -y install \
    git \
    make \
    gdal-bin \
    build-essential \
    g++ \
    libsqlite3-0 \
    libsqlite3-dev \
    zlib1g-dev \
    python3 \
    python3-pip \
    python3-venv \
    python3-gdal \
    jq && \
  mkdir -p /tmp/build && cd /tmp/build && \
  git clone https://github.com/felt/tippecanoe.git && \
  cd tippecanoe && \
  make -j2 && \
  make install && \
  cd /tmp && \
  rm -r /tmp/build && \
  rm -rf /var/lib/apt/lists/* && \
  apt-get remove -y git make build-essential g++ zlib1g-dev libsqlite3-dev && \
  apt-get autoremove -y && \
  mkdir /app

WORKDIR /app
ADD . .

RUN python3 -m venv --system-site-packages .venv && \
  . .venv/bin/activate && \
  pip install --upgrade pip && \
  pip install .

ENTRYPOINT [ "./entrypoint.sh" ]
