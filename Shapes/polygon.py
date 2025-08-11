from Geometry.point import Point
from Shapes.shapes import Shape
class Polygon(Shape):
    def __init__(self, Points, color="black", line_width=1,outline="black"):
        super().__init__(color=color, width=line_width)
        self.points = Points
        self.outline = outline
    
    def draw(self, pen):
        if not self.points:
            return
        #pen.move_to(self.points[0].x, self.points[0].y)
        #for point in self.points[1:]:
         #  pen.line_to(point.x, point.y)
        #pen.line_to(self.points[0].x, self.points[0].y)
        #drawing the polygon using built-in canvas method
        pen._canvas.draw_polygon(self.points, outline=self.outline, fill=self._color, width=self._width)
    def __str__(self):
        return f"Polygon(points={self.points}, color={self._color}, line_width={self._width})"
    def __repr__(self):
        return str(self)