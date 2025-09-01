from Drawing.canvas import Canvas
from Geometry.line import Line
from Drawing.pen import Pen
from Shapes.circle import Circle
from Shapes.polygon import Polygon
from Shapes.rectangle import Rectangle
from Geometry.point import Point
import tkinter as tk
class Visualizer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Shape Drawing Application")

        self.tk_canvas = tk.Canvas(self.root, width=500, height=500, bg="white")
        self.tk_canvas.pack()

        self.canvas = Canvas(self.tk_canvas)
        self.pen = Pen(self.canvas, fill="black", width=2)

        self.root.bind("c", lambda event: self.canvas.clear())

    def run_visualizer(self):
        print("Drawing a Circle")
        circle = Circle(Point(100, 100), 50, outline="black", width=2)
        circle.draw(self.pen)

        print("Drawing a Rectangle")
        rectangle = Rectangle(Point(200, 50), length=100.0, height=60.0,  outline="black", width=2)
        rectangle.draw(self.pen)

        print("Drawing a Polygon")
        triangle = Polygon(Point(150, 250), base=100, height=100, outline="black", width=2)
        triangle.draw(self.pen)

        print("Drawing Lines:")
        lines = [
            Line(Point(50, 300), Point(150, 300)),
            Line(Point(180, 300), Point(280, 300)),
            Line(Point(310, 300), Point(410, 300))
        ]
        for line in lines:
            self.canvas.add_line(line.start, line.end, fill="black", width=2)

        self.root.mainloop()