from Geometry.point import Point
class Pen:
    def __init__(self, canvas, fill="black",width = 5):
        self._width = width
        self._fill = fill
        self._canvas = canvas
        self._current_pos = Point(0, 0)

    def move_to(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Coordinates must be numbers")
        self._current_pos = Point(x, y)

    def line_to(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Coordinates must be numbers")
        new_pos = Point(x, y)
        self._canvas.add_line(self._current_pos, new_pos, fill=self._fill, width=self._width)
        self._current_pos = new_pos
    
    def get_position(self):
        return self._current_pos
    
    def __str__(self):
        return f"Pen(fill={self._fill}, width={self._width})"

    def __repr__(self):
        return f"Pen(fill={self._fill!r}, width={self._width})"
   