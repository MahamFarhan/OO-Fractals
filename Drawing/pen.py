from Geometry.point import Point
class Pen:
    def __init__(self, canvas,color = "black", width = 5 ,style = "solid"):
        self._color = color
        self._width = width
        self._style = style
        self._canvas = canvas
        self._current_pos = Point(0,0)

    def move_to(self, x, y):
        self._current_pos = Point(x, y)

    def line_to(self, x, y):
        new_pos = Point(x, y)
        self._canvas.add_line(self._current_pos, new_pos,color=self._color, width=self._width, style=self._style)
        self._current_pos = new_pos

    def get_position(self):
        return self._current_pos
    #Returns the current position as a Point object. Useful for checking where the pen is.
    def __str__(self):
        return f"Pen(color={self._color}, width={self._width}, style={self._style})"

    def __repr__(self):
        return f"Pen(color={self._color!r}, width={self._width}, style={self._style!r})"
   