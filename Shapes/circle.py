from Shapes.shapes import Shape
from Geometry.point import Point
import math
from Geometry.vector2D import vector2D
class Circle(Shape):
    # inherits from Shape class to draw a circle
    def __init__(self, center: Point, radius: float, color="black", width=1):
        super().__init__(color, width)
        self._center = center
        self._radius = radius
    @property
    def center(self):
        return self._center
    @property
    def radius(self):
         return self._radius
    def draw(self, pen):
        x = self._center.x
        y = self._center.y
        r = self._radius
        pen._canvas.draw_circle(x, y, r,outline=self._color, fill=self._color)

    def __str__(self):
        return f"Circle(center={self.center}, radius={self.radius}, color={self.color}, width={self.width})"

    def __repr__(self):
        return str(self)