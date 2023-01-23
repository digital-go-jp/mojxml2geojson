# coding: utf-8


def GetCrs(crsText: str):
    crsTable = {
        '任意座標系': '0',
        '公共座標1系': '2443',
        '公共座標2系': '2444',
        '公共座標3系': '2445',
        '公共座標4系': '2446',
        '公共座標5系': '2447',
        '公共座標6系': '2448',
        '公共座標7系': '2449',
        '公共座標8系': '2450',
        '公共座標9系': '2451',
        '公共座標10系': '2452',
        '公共座標11系': '2453',
        '公共座標12系': '2454',
        '公共座標13系': '2455',
        '公共座標14系': '2456',
        '公共座標15系': '2457',
        '公共座標16系': '2458',
        '公共座標17系': '2459',
        '公共座標18系': '2460',
        '公共座標19系': '2461'
    }

    if ('0' == crsTable[crsText]):
        #return crsTable[crsText], 'urn:ogc:def:crs:OGC:1.3:CRS84'
        return crsTable[crsText], None
    else:
        return crsTable[crsText], 'urn:ogc:def:crs:EPSG::' + crsTable[crsText]
