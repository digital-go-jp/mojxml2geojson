# coding: utf-8

from geojson import Feature, FeatureCollection, MultiPolygon
import geojson
import itertools

import package.ConvertDatum as ConvertDatum
import package.PointOnSurface as PointOnSurface


def MojXMLtoGeoJSON(mojObj: dict, exclude_flag):

    IdHudeTable = mojObj['mojXmlPolygon']['IdHudeTable']
    IdSurfaceTable = mojObj['mojXmlPolygon']['IdSurfaceTable']

    feature_list = []
    crs_name = None

    for key in IdHudeTable.keys():
        hude = IdHudeTable[key]
        ref_gm_surface = hude['形状']['@idref']

        hude_property = setExistProperties(hude,
                                           ['@id', '地図番号', '縮尺分母', '大字コード', '丁目コード', '小字コード', '予備コード', '大字名', '丁目名', '小字名', '予備名', '地番', '精度区分', '座標値種別', '筆界未定構成筆'],
                                           ['筆ID', '地図番号', '縮尺分母', '大字コード', '丁目コード', '小字コード', '予備コード', '大字名', '丁目名', '小字名', '予備名', '地番', '精度区分', '座標値種別', '筆界未定構成筆'])

        # 地番が地区外、別図のデータを出力しない
        if exclude_flag is True:
            if ('地区外' in hude_property['地番']) or ('別図' in hude_property['地番']):
                continue

        xml_property = setExistProperties(mojObj,
                                          ['version', 'crs', 'datum_type', 'map_name', 'city_code', 'city_name'],
                                          ['version', '座標系', '測地系判別', '地図名', '市区町村コード', '市区町村名'])

        sorted_properties = sortProperties(dict(**xml_property, **hude_property),
                                           ['筆ID',
                                            'version',
                                            '座標系',
                                            '測地系判別',
                                            '地図名',
                                            '地図番号',
                                            '縮尺分母',
                                            '市区町村コード',
                                            '市区町村名',
                                            '大字コード',
                                            '丁目コード',
                                            '小字コード',
                                            '予備コード',
                                            '大字名',
                                            '丁目名',
                                            '小字名',
                                            '予備名',
                                            '地番',
                                            '精度区分',
                                            '座標値種別',
                                            '筆界未定構成筆'])

        # 地図のプロパティと各筆のプロパティをマージ
        # feature = Feature(properties=dict(**xml_property, **hude_property))
        feature = Feature(properties=sorted_properties)

        # 連続で重複している要素を削除
        exterior = [k for k, g in itertools.groupby(IdSurfaceTable[ref_gm_surface]['exterior'])]
        interior = IdSurfaceTable[ref_gm_surface]['interior']
        if len(interior) > 0:
            interior = [k for k, g in itertools.groupby(IdSurfaceTable[ref_gm_surface]['interior'])]
            for i in range(len(interior)):
                interior[i] = [k for k, g in itertools.groupby(interior[i])]

        crs_name = mojObj['named_crs']

        # 測地系の変換 to 6668(JGD2011)
        if crs_name is not None:  # 任意座標は測地系の変換をしない
            exterior = ConvertDatum.xy2bl(exterior, mojObj['number_crs'], 6668)
            if len(interior) > 0:
                for i in range(len(interior)):
                    interior[i] = ConvertDatum.xy2bl(interior[i], mojObj['number_crs'], 6668)
            crs_name = 'urn:ogc:def:crs:EPSG::6668'

        if len(interior) == 0:
            feature['geometry'] = {'type': 'MultiPolygon',
                                   'coordinates': [[exterior],], }
        elif len(interior) > 0:
            coord = []
            coord.append(exterior)
            for i in interior:
                coord.append(i)
            feature['geometry'] = {'type': 'MultiPolygon',
                                   'coordinates': [coord], }
        feature = PointOnSurface.PointOnSurface(feature)
        feature_list.append(feature)

    feature_collection = FeatureCollection(feature_list)
    if crs_name is not None:
        feature_collection['crs'] = {'properties': {'name': crs_name}, 'type': 'name'}
    else:
        feature_collection['crs'] = crs_name

    return geojson.dumps(feature_collection, ensure_ascii=False)


def setExistProperties(obj, from_key_list, to_key_list):
    tmp_obj = {}
    for key in from_key_list:
        if key in obj.keys():
            i = from_key_list.index(key)
            tmp_obj[to_key_list[i]] = obj[key]
        else:
            i = from_key_list.index(key)
            tmp_obj[to_key_list[i]] = None

    return tmp_obj


def sortProperties(obj, sort_key_list):
    tmp_obj = {}
    for key in sort_key_list:
        if key in obj.keys():
            i = sort_key_list.index(key)
            tmp_obj[sort_key_list[i]] = obj[key]
        else:
            i = sort_key_list.index(key)
            tmp_obj[sort_key_list[i]] = None

    return tmp_obj
