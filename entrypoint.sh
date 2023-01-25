#!/bin/bash -e

. .venv/bin/activate

exec mojxml2geojson "$@"
