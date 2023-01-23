# coding: utf-8

from pyproj import Transformer
from decimal import Decimal, ROUND_HALF_UP


def xy2bl(coordinates, from_epsg, to_epsg):
    tr = Transformer.from_proj(from_epsg, to_epsg)
    bl_list = []
    for coord in coordinates:
        lat, lon = tr.transform(coord[1], coord[0])
        # 小数点9桁に丸める
        lat = Decimal(str(lat)).quantize(Decimal('0.000000001'), rounding=ROUND_HALF_UP)
        lon = Decimal(str(lon)).quantize(Decimal('0.000000001'), rounding=ROUND_HALF_UP)
        bl_list.append([float(lon), float(lat)])
    return bl_list
