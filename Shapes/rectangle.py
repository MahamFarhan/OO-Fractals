from Geometry.point import Point
from Shapes.shapes import Shape
from Drawing.pen import Pen
class Rectangle(Shape):
    def __init__(self, point:Point, length: float, height: float, outline="black",width=1):
        super().__init__( outline=outline, width=width)
        self.point = point
        self.length = length
        self.height = height
    
    def draw(self, pen: Pen):
     p1 = self.point
     p2 = Point(p1.x + self.length, p1.y)
     p3 = Point(p2.x, p2.y + self.height)
     p4 = Point(p1.x, p1.y + self.height)

     pen.move_to(p1.x, p1.y)
     pen.line_to(p2.x, p2.y)
     pen.line_to(p3.x, p3.y)
     pen.line_to(p4.x, p4.y)
     pen.line_to(p1.x, p1.y)
       
       

    