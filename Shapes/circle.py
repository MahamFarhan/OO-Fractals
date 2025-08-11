from Shapes.shapes import Shape
from Geometry.point import Point
import math
class Circle(Shape):
    # inherits from Shape class to draw a circle
    def __init__(self, center: Point, radius: float, color="black",outline="black",fill=None ,width=1):
        super().__init__(color=color, width=width)
         # center is a Point object, radius is a float
         # color is the color of the circle, outline is the outline color, fill is the fill color (optional)
        self._center = center
        self._radius = radius
        self.outline = outline
        self.fill = fill  # Optional fill color, can be None if not filled
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
        pen._canvas.draw_circle(x, y, r,outline=self._color, fill=self._color, width=self._width)

    def __str__(self):
        return f"Circle(center={self.center}, radius={self.radius}, color={self.color}, width={self.width})"

    def __repr__(self):
        return str(self)