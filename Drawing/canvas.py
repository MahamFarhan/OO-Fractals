from Geometry.point import Point
from Geometry.line import Line

class Canvas:
    def __init__(self, tk_canvas):
        self.canvas = tk_canvas
        self._lines = []

    def add_line(self, p1:Point, p2:Point, fill="black", width=1):
        line = Line(p1,p2)
        self._lines.append(line)
        self.canvas.create_line(
        line.start.x, line.start.y,
        line.end.x, line.end.y,
        fill=fill,
        width=width,
    )  

    def start(self):
        self.root.mainloop()
    def clear(self):
        self.canvas.delete("all")
        self._lines = []

    def __str__(self):
        return f"Canvas with {len(self._lines)} lines"

    def __repr__(self):
        return f"Canvas(lines={self._lines})"


	