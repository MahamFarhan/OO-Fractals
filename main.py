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
    

    app = App(root, canvas, start_position=(500, 400))

    # Fixed input (square path)
    app.pen.penup()
    app.pen.move_to(450, 450)   # move square to top-left
    app.pen.pendown()
    fixed_commands = "F+F+F+F"
    print(f"Running fixed commands: {fixed_commands}")
    app.run(fixed_commands)

    # Fixed input (zigzag path)
    app.pen.penup()
    app.pen.move_to(400, 400)   # move zigzag to center-right
    app.pen.pendown()
    zigzag_commands = "F-F+F-F"
    print(f"Running zigzag commands: {zigzag_commands}")
    app.run(zigzag_commands)

    # User input (command string)
    user_commands = input("Enter drawing commands (e.g., F+F-F+F): ")
    if user_commands.strip():
        app.pen.penup()
        app.pen.move_to(250, 450)   # place user drawing lower center
        app.pen.pendown()
        print(f"Running user commands: {user_commands}")
        app.run(user_commands)    

    root.mainloop()


if __name__ == "__main__":
    main()