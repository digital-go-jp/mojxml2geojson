# coding: utf-8


def MojXmlPolygon(xml_dict: dict):
    IdPointTable = GetIdPointTable(xml_dict)
    IdCurveTable = GetIdCurveTable(xml_dict, IdPointTable)
    IdSurfaceTable = GetIdSurfaceTable(xml_dict, IdCurveTable)
    IdHudeTable = GetIdHudeTable(xml_dict)

    mojObj = {'IdPointTable': IdPointTable,
              'IdCurveTable': IdCurveTable,
              'IdSurfaceTable': IdSurfaceTable,
              'IdHudeTable': IdHudeTable
              }
    return mojObj


def GetIdPointTable(xml_dict: dict):
    IdPointTable = {}
    for xy in xml_dict['地図']['空間属性']['zmn:GM_Point']:
        id = xy['@id']
        # x,y : -999999.999 <= 値 <= 999999.999, 小数部桁数 <= 3
        x = xy['zmn:GM_Point.position']['zmn:DirectPosition']['zmn:X']
        y = xy['zmn:GM_Point.position']['zmn:DirectPosition']['zmn:Y']
        IdPointTable[id] = [float(y), float(x)]
    return IdPointTable


def GetIdCurveTable(xml_dict: dict, IdPointTable: dict):
    IdCurveTable = {}
    for pRef in xml_dict['地図']['空間属性']['zmn:GM_Curve']:
        id = pRef['@id']
        IdCurveTable[id] = []
        gm_position = pRef['zmn:GM_Curve.segment']['zmn:GM_LineString']['zmn:GM_LineString.controlPoint']['zmn:GM_PointArray.column']

        # 地図XML 別10-39
        for point in gm_position:
            if point.get('zmn:GM_Position.indirect') is not None:
                point_id = (point['zmn:GM_Position.indirect']
                                 ['zmn:GM_PointRef.point']
                                 ['@idref'])
                IdCurveTable[id].append(IdPointTable[point_id])
            elif point.get('zmn:GM_Position.direct') is not None:
                x = point['zmn:GM_Position.direct']['zmn:X']
                y = point['zmn:GM_Position.direct']['zmn:Y']
                IdCurveTable[id].append([float(y), float(x)])
    return IdCurveTable


def GetIdSurfaceTable(xml_dict: dict, IdCurveTable: dict):
    IdSurfaceTable = {}

    # 要素が1つでlistでない場合listにする
    if type(xml_dict['地図']['空間属性']['zmn:GM_Surface']) is not list:
        xml_dict['地図']['空間属性']['zmn:GM_Surface'] = [xml_dict['地図']['空間属性']['zmn:GM_Surface']]

    for cRef in xml_dict['地図']['空間属性']['zmn:GM_Surface']:
        id = cRef['@id']
        IdSurfaceTable[id] = []
        gm_surfaceboundary = cRef['zmn:GM_Surface.patch']['zmn:GM_Polygon']['zmn:GM_Polygon.boundary']['zmn:GM_SurfaceBoundary']
        pos_obj = {'exterior': [], 'interior': []}

        # 地図XML 別10-44
        # 外部境界
        gm_ring = gm_surfaceboundary['zmn:GM_SurfaceBoundary.exterior']['zmn:GM_Ring']['zmn:GM_CompositeCurve.generator']
        for exterior in gm_ring:
            exterior_id = (exterior['@idref'])
            for pos in IdCurveTable[exterior_id]:
                pos_obj['exterior'].append(pos)

        # 内部境界
        if gm_surfaceboundary.get('zmn:GM_SurfaceBoundary.interior') is not None:
            if type(gm_surfaceboundary['zmn:GM_SurfaceBoundary.interior']) is not list:
                gm_surfaceboundary['zmn:GM_SurfaceBoundary.interior'] = [gm_surfaceboundary['zmn:GM_SurfaceBoundary.interior']]

            gm_ring_list = gm_surfaceboundary['zmn:GM_SurfaceBoundary.interior']
            for gm_ring in gm_ring_list:
                interior_list = []
                for interior in gm_ring['zmn:GM_Ring']['zmn:GM_CompositeCurve.generator']:
                    interior_id = (interior['@idref'])
                    for pos in IdCurveTable[interior_id]:
                        interior_list.append(pos)
                    pos_obj['interior'].append(interior_list)

        IdSurfaceTable[id] = pos_obj

    return IdSurfaceTable


def GetIdHudeTable(xml_dict: dict):
    IdHudeTable = {}

    # 要素が1つでlistでない場合listにする
    if type(xml_dict['地図']['主題属性']['筆']) is not list:
        xml_dict['地図']['主題属性']['筆'] = [xml_dict['地図']['主題属性']['筆']]

    for hRef in xml_dict['地図']['主題属性']['筆']:
        id = hRef['@id']
        IdHudeTable[id] = hRef

    if '図郭' in xml_dict['地図'].keys():
        # 要素が1つでlistでない場合listにする
        if type(xml_dict['地図']['図郭']) is not list:
            xml_dict['地図']['図郭'] = [xml_dict['地図']['図郭']]

        for zRef in xml_dict['地図']['図郭']:
            if '筆参照' in zRef.keys():
                # 要素が1つでlistでない場合listにする
                if type(zRef['筆参照']) is not list:
                    zRef['筆参照'] = [zRef['筆参照']]
                for hRef in zRef['筆参照']:
                    idref = hRef['@idref']
                    IdHudeTable[idref]['地図番号'] = zRef['地図番号']
                    if '縮尺分母' in zRef.keys():
                        IdHudeTable[idref]['縮尺分母'] = zRef['縮尺分母']

    return IdHudeTable
