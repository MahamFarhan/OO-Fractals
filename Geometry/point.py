from Geometry.vector2D import vector2D 
class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y
    @property
    def x (self):
        return self._x
    @x.setter
    def x (self, value):
        self._x = value
    @property
    def y (self):
        return self._y
    @y.setter
    def y (self, value):
        self._y = value
    def translate(self, vector: vector2D):
        return Point(self._x + vector._dx, self._y + vector._dy)   
    def as_tuple(self):
        return (self._x, self._y) 
    def __str__(self):
        return f"Point({self._x}, {self._y})"
    def __repr__(self):
        return f"Point(x={self._x}, y={self._y})"
        