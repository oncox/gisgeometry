from abc import ABC, abstractmethod
from osgeo import ogr

class GeometryComponent(ABC):
    @abstractmethod
    def __init__(self):
        self.__geom = None



class Point(GeometryComponent):
    def __init__(self):
        GeometryComponent.__init__(self)
        self.__geom = ogr.Geometry(ogr.wkbPoint)

class LineString(GeometryComponent):
    def __init__(self):
        GeometryComponent.__init__(self)
        self.__geom = ogr.Geometry(ogr.wkbLineString)

class Polygon(GeometryComponent):
    def __init__(self):
        GeometryComponent.__init__(self)
        self.__geom = ogr.Geometry(ogr.wkbPolygon)
