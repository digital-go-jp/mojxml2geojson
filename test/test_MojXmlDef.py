import package.MojXmlDef


def test():
    assert package.MojXmlDef.GetCrs('任意座標系') == ('0', None)
    assert package.MojXmlDef.GetCrs('公共座標19系') == ('2461', 'urn:ogc:def:crs:EPSG::2461')
