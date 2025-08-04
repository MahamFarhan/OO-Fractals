from .point import Point
import math
class Line:
    def __init__(self , start=Point, end=Point):
        self.start = start
        self.end = end
    @property
    def start(self):
        return self._start
    @start.setter
    def start(self, value):
        self._start = value
    @property
    def end(self):
        return self._end
    @end.setter
    def end(self, value):
        self._end = value
    @property
    def length(self):
        dx = self.end.x - self.start.x
        dy = self.end.y - self.start.y
        return math.sqrt(dx ** 2 + dy ** 2)
    def __str__(self):
        return f"Line(start={self.start}, end={self.end})"
    def __repr__(self):
        return f"Line(start={self.start}, end={self.end})"
    