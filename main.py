from Geometry.point import Point
from Geometry.line import Line
from Drawing.pen import Pen
from Drawing.canvas import Canvas
from Shapes.circle import Circle
from Shapes.polygon import Polygon
from Shapes.rectangle import Rectangle


def main():
    canvas = Canvas(width=500, height=500)
    pen = Pen(canvas)
    canvas.clear()

    print("Drawing a Circle:")
    circle = Circle(center=Point(200,200), radius=50, color="blue",width=2)
    circle.draw(pen)

    print("Drawing a Polygon:")
    polygon = Polygon(center=Point(100, 100), radius=40, sides=5, color="pink", width=2)
    polygon.draw(pen)

    print("Drawing a Rectangle:")
    rectangle = Rectangle(top_left=Point(250, 50), width=100, height=60, color="yellow", line_width=2)
    rectangle.draw(pen)

    canvas.draw_line(Line(Point(50, 300), Point(150, 300)))
    canvas.draw_line(Line(Point(180, 300), Point(280, 300)))
    canvas.draw_line(Line(Point(310, 300), Point(410, 300)))
    canvas.start()

    print("Canvas after drawing:")
    print(canvas)

    for line in canvas.lines:
        print(line)

if __name__ == "__main__":
    main()
    
