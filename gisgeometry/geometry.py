from abc import ABC, abstractmethod
from osgeo import ogr

class GeometryComponent(ABC):

    __mappings = {
        'postgresql':{'bool':'boolean', 'str': 'text', 'float': 'real', 'int': 'integer', 'long': 'bigint'}
    }

    @abstractmethod
    def __init__(self, geomType, srid=4326):
        self.__geom = ogr.Geometry(geomType)
        self.__attributes = {}
        self.__srid = srid

    def __setitem__(self, key, value):
        self.__attributes[key] = value

    def __getitem__(self, key):
        return self.__attributes[key]

    def __delitem__(self, key):
        del self.__attributes[key]

    def __repr__(self):
        return self.WriteWKT()

    def __str__(self):
        return self.__repr__()

    def WriteWKT(self):
        return self.__geom.ExportToWkt()

    def WriteWKB(self):
        return self.__geom.ExportToWkb()

    def AddPoint(self, x, y):
        self.__geom.AddPoint(x, y)

    def CreateTable(self, tableName):

        columns = []

        for key, value in self.__attributes.items():
                columns.append("'{}' {}".format(key, self.__mappings['postgresql'][value.__class__.__name__]))

        return 'CREATE TABLE "{}"({})'.format(tableName, ', '.join(columns))

class Point(GeometryComponent):
    def __init__(self, **kwargs):
        GeometryComponent.__init__(self, ogr.wkbPoint, **kwargs)

class LineString(GeometryComponent):
    def __init__(self):
        GeometryComponent.__init__(self, ogr.wkbLineString)

class Polygon(GeometryComponent):
    def __init__(self):
        GeometryComponent.__init__(self, ogr.wkbPolygon)
