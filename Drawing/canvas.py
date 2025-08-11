from Geometry.point import Point
from Geometry.line import Line
import tkinter as tk
class Canvas:
    def __init__(self, tk_canvas):
        self.canvas = tk_canvas
        self._lines = []

    def add_line(self, p1:Point, p2:Point,color="black", width=1, style="solid"):
        line = Line(p1,p2)
        self._lines.append(line)
        dash_style = (4,2)if style == 'dashed' else None
        self.canvas.create_line(
            p1.x, p1.y, p2.x, p2.y,
            fill=color,
            width=width,
            dash=dash_style
    )
    def draw_line(self, line: Line, color="black", width=1, style="solid"):
        """Draws a Line object on the canvas and stores it."""
        self._lines.append(line)
        dash_style = (4, 2) if style == 'dashed' else None
        self.canvas.create_line(
            line.start.x, line.start.y,
            line.end.x, line.end.y,
            fill=color,
            width=width,
            dash=dash_style
        )
    
    def draw_circle(self, x, y, radius, outline="black", fill="",width=1):
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline=outline, fill=fill, width=width)

    def draw_rectangle(self, x1, y1, x2, y2, outline="black", fill="", width=1):
        self.canvas.create_rectangle(x1, y1, x2, y2, outline=outline, fill=fill, width=width)
    
    def draw_polygon(self, points, outline="black", fill="",width=1):
        flat_points = [coord for point in points for coord in point.as_tuple()]
        self.canvas.create_polygon(flat_points, outline=outline, fill=fill, width=width)
    def start(self):
        self.root.mainloop()
    def clear(self):
        self.canvas.delete("all")
        self._lines = []

    def __str__(self):
        return f"Canvas with {len(self._lines)} lines"

    def __repr__(self):
        return f"Canvas(lines={self._lines})"


	