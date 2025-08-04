from Geometry.point import Point
import math
from Shapes.shapes import Shape
from Geometry.vector2D import vector2D
class Polygon(Shape):
    def __init__(self, center: Point, radius: float, sides: int, color="black", width=1):
        super().__init__(color, width)
        self._center = center
        self._radius = radius
        self._sides = sides
    @property
    def center(self):
        return self._center

    @property
    def radius(self):
        return self._radius

    @property
    def sides(self):
        return self._sides

    def draw(self, pen):
        angle_step = 2 * math.pi / self._sides
        points = []
        for i in range(self._sides):
            angle = i * angle_step
            x = self._center.x + self._radius * math.cos(angle)
            y = self._center.y + self._radius * math.sin(angle)
            points.append(Point(x, y))
        pen._canvas.draw_polygon(points, outline=self._color, fill=self._color)

    def __str__(self):
        return f"Polygon(sides={self.sides}, center={self.center}, radius={self.radius})"
