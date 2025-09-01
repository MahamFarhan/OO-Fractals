from .point import Point
class Line:
    def __init__(self , start=Point, end=Point):
        self.start = start
        self.end = end
    #this does not store the value of start and end as protected attributes
    #we are not using a underscore here because python routes it to the property methods then we validate the input
    #and set the values in the setter methods which are protected
    @property
    def start(self):
        return self._start
    @start.setter
    def start(self, value):
        if not isinstance(value, Point):
            raise TypeError("Start must be a Point")
        self._start = value
    @property
    def end(self):
        return self._end
    @end.setter
    def end(self, value):
        if not isinstance(value, Point):
            raise TypeError("End must be a Point")
        self._end = value
    def length(self):
        return self._start.distance(self.end)
    #A method that returns the distance between the start and end points.
    # It delegates the work to the distance() method of your Point class:
    def __str__(self):
         return f"Line({self.start} → {self.end})"
    def __repr__(self):
        return f"Line(start={self.start!r}, end={self.end!r})"
    