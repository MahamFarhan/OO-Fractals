from Geometry.point import Point
from Geometry.line import Line
import tkinter as tk
class Canvas:
    def __init__(self, width=800, height=600):
        self.root = tk.Tk()
        self.root.title("Drawing Canvas")
        self.canvas = tk.Canvas(self.root, width=width, height=height, bg="white")
        self.canvas.pack()
        self._lines = []
        self.root.bind("c", lambda event: self.clear())

    def draw_line(self, line, color="black", width=2):
        self._lines.append(line)
        self.canvas.create_line(
        line.start.x, line.start.y,
        line.end.x, line.end.y,
        fill=color,
        width=width
    )
    @property
    def lines(self):
        return self._lines

    def draw_circle(self, x, y, radius, outline="black", fill=""):
         self.canvas.create_oval(
        x - radius, y - radius,
        x + radius, y + radius,
        outline=outline,
        fill=fill,
        width=2
    )
    def draw_rectangle(self, x1, y1, x2, y2, outline="black", fill=""):
        self.canvas.create_rectangle(x1, y1, x2, y2, outline=outline, fill=fill, width=2)
    
    def draw_polygon(self, points, outline="black", fill=""):
        flat_points = [coord for point in points for coord in point.as_tuple()]
        self.canvas.create_polygon(flat_points, outline=outline, fill=fill)
    def start(self):
        self.root.mainloop()
    def clear(self):
        self.canvas.delete("all")
        self._lines = []
    def mainloop(self):
        self.root.mainloop()

    def __str__(self):
        return f"Canvas with {len(self._lines)} lines"

    def __repr__(self):
        return f"Canvas(lines={self._lines})"


	