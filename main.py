from Geometry.point import Point
from Geometry.line import Line
from Drawing.pen import Pen
from Drawing.canvas import Canvas
from Shapes.circle import Circle
from Shapes.polygon import Polygon
from Shapes.rectangle import Rectangle
from App.app import App
import tkinter as tk
def main():
    root = tk.Tk()
    root.title("Drawing Application")

    tk_canvas = tk.Canvas(root, width=800, height=600, bg="white")
    tk_canvas.pack()


    canvas = Canvas(tk_canvas)
    root.bind("c", lambda event: canvas.clear())
    
    pen = Pen(canvas)
    
    print("Drawing a Circle:")
    circle = Circle(center=Point(200,200), radius=50, color="blue",outline="black",width=2)
    circle.draw(pen)

    print("Drawing a Polygon:")
    polygon = Polygon(Points=[Point(100, 145), Point(160,60), Point(220,145)], color="pink",outline="black", line_width=2)
    polygon.draw(pen)

    print("Drawing a Rectangle:")
    rectangle = Rectangle(top_left=Point(250, 50), width=150, height=100, color="yellow", outline ="black", line_width=2)
    rectangle.draw(pen)

    print("Drawing Lines:")
    lines = [
    Line(Point(50, 300), Point(150, 300)),
    Line(Point(180, 300), Point(280, 300)),
    Line(Point(310, 300), Point(410, 300))
 ]
    for line in lines:
        canvas.add_line(line.start,line.end, color="black", width=2, style="solid")
    

    print("Canvas after drawing:")
    print(canvas)
    print("Pen position:", pen.get_position())
    app = App(root,canvas, start_position=(500, 400))
    app.run()
    
    root.mainloop()

if __name__ == "__main__":
    main()
    
