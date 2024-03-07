from shapely.geometry import shape


def geometry_to_wkt(geometry):
    return shape(geometry).wkt
