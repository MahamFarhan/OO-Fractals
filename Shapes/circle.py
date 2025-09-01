from Shapes.shapes import Shape
from Geometry.point import Point
from Drawing.pen import Pen
import math
class Circle(Shape):
    # inherits from Shape class to draw a circle
    def __init__(self, center: Point, radius: float, outline="black" ,width=1):
        super().__init__(outline=outline, width=width)
        # center is a Point object, radius is a float
        # color is the color of the circle, outline is the outline color, fill is the fill color (optional)
        self._center = center
        self._radius = radius
    @property
    def center(self):
        return self._center
    @property
    def radius(self):
         return self._radius
    
    def Area(self):
        #Return the area of the circle
        return math.pi * (self.radius ** 2)
    def draw(self, pen:Pen):
        x = self._center.x
        y = self._center.y
        r = self._radius
        pen._canvas.canvas.create_oval(x-r, y-r, x+r, y+r, outline=self.outline, width=self._width)

