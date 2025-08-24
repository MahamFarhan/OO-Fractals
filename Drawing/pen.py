from Geometry.point import Point
import math
class Pen:
    def __init__(self, canvas,color = "black", width = 5 ,style = "solid", position = (0,0), heading = 0):
        self._color = color
        self._width = width
        self._style = style
        self._canvas = canvas
        self._current_pos = Point(*position) if isinstance(position, tuple) else position  
        self._heading = heading  # in degrees, 0 is to the right
        self._pen_down = True

    def move_to(self, x, y):
        self._current_pos = Point(x, y)

    def line_to(self, x, y):
        new_pos = Point(x, y)
        self._canvas.add_line(self._current_pos, new_pos,color=self._color, width=self._width, style=self._style)
        self._current_pos = new_pos
    
    def forward(self, distance):
        #Move pen forward in current angle, drawing a line.
        rad = math.radians(self._heading)
        new_x = self._current_pos.x + distance * math.cos(rad)
        new_y = self._current_pos.y - distance * math.sin(rad)  
        self.line_to(new_x, new_y)
    
    def turn_left(self, angle):
        #Rotate pen left (counterclockwise).
         self._heading = (self._heading + angle) % 360
    
    
    def turn_right(self, angle):
        # Rotate pen right (clockwise).
        self._heading = (self._heading - angle) % 360

    def turn(self, angle):
        # Generic turn (positive = left, negative = right).
        self._heading = (self._heading + angle) % 360

    def get_heading(self):
        #Returns the current heading in degrees.
        return self._heading
    def penup(self):
        self._pen_down = False
    def pendown(self):
        self._pen_down = True

    def get_position(self):
        return self._current_pos
    #Returns the current position as a Point object. Useful for checking where the pen is.
    def __str__(self):
        return f"Pen(color={self._color}, width={self._width}, style={self._style}, heading={self._heading})"

    def __repr__(self):
        return f"Pen(color={self._color!r}, width={self._width}, style={self._style!r}, heading={self._heading})"
   