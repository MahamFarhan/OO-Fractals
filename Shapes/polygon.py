from Geometry.point import Point
from Shapes.shapes import Shape
from Drawing.pen import Pen
class Polygon(Shape):
    def __init__(self, point:Point, base: float, height: float, outline="black",width=1):
        super().__init__(outline=outline,width=width)
        self.point = point
        self.base = base
        self.height = height
    
    def draw(self, pen: Pen):
     x = self.point.x
     y = self.point.y
     base = self.base
     height = self.height

     pen.move_to(x, y)
     pen.line_to(x+base, y)
     pen.line_to(x+base/2, y-height)
     pen.line_to(x, y)