# coding: utf-8

from osgeo import ogr
import json
from decimal import Decimal, ROUND_HALF_UP


def PointOnSurface(feature: dict):
    geom = ogr.CreateGeometryFromJson(json.dumps(feature['geometry']))
    point_on_surface = geom.PointOnSurface()
    lat = point_on_surface.GetY()
    lon = point_on_surface.GetX()
    lat = Decimal(str(lat)).quantize(Decimal('0.000000001'), rounding=ROUND_HALF_UP)
    lon = Decimal(str(lon)).quantize(Decimal('0.000000001'), rounding=ROUND_HALF_UP)
    feature['properties']['代表点緯度'] = float(lat)
    feature['properties']['代表点経度'] = float(lon)

    return feature
