import json


def get_geometry_from_polygon_file(file):
    polygon = json.load(file.file)
    return polygon["features"][0]["geometry"]
