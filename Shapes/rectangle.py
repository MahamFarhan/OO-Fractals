from Geometry.point import Point
from Shapes.shapes import Shape
from Geometry.vector2D import vector2D
class Rectangle(Shape):
    def __init__(self, top_left: Point, width: float, height: float, color="black", line_width=1):
        super().__init__(color=color, width=line_width)
        self.top_left = top_left
        self.rect_width = width
        self.rect_height = height

    def draw(self, pen):
        x1 = self.top_left.x
        y1 = self.top_left.y
        x2 = x1 + self.rect_width
        y2 = y1 + self.rect_height
        pen._canvas.draw_rectangle(x1, y1, x2, y2, outline=self._color, fill=self._color)


    def __str__(self):
        return f"Rectangle(top_left={self.top_left}, width={self.rect_width}, height={self.rect_height}, color={self.color}, line_width={self.width})"

    def __repr__(self):
        return str(self)