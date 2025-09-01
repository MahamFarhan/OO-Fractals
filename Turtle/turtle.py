from Drawing.pen import Pen 
from Geometry.point import Point
import math
class Turtle:
    def __init__(self, pen: Pen, position=None, start_x = 0,start_y=0, heading=0):
        if not isinstance(pen, Pen):
            raise TypeError("pen must be an instance of Pen")
        # validation that pen is a Pen object
        self._pen = pen
        
        #starting position
        #If a position (Point or tuple) is given = validate it
        #Otherwise = use start_x, start_y
        if position is not None:
            self._position = self.validate_position(position)
        else:
            self._position = Point(start_x, start_y)
        
        # validating angle
        self._heading = self.validate_heading(heading)
        self._pendown = True
        # intially pen is down (ready to draw)

        # Move pen to starting point
        self._pen.move_to(self._position.x, self._position.y)

    # -------- Property Decorators --------
    @property
    def position(self):
        return self._position
    #returns the turtle current position

    @position.setter
    def position(self, pos):
        pos = self.validate_position(pos)
        self._position = pos
        self._pen.move_to(pos.x, pos.y)
        #updates position after validation and moves the pen there

    @property
    def heading(self):
        return self._heading
    #returns the current heading

    @heading.setter
    def heading(self, angle):
        self._heading = self.validate_heading(angle)
    
    # -------- Validations --------
    def validate_position(self, pos):
       # If tuple provided, convert to Point
        if isinstance(pos, tuple) and len(pos) == 2:
            pos = Point(pos[0], pos[1])

        if not isinstance(pos, Point):
            raise TypeError("position must be a Point or a tuple (x, y)")
        #if its not a point raise an error

        if not isinstance(pos.x, (int, float)) or not isinstance(pos.y, (int, float)):
            raise TypeError("position coordinates must be numbers")
        return pos
        #checking that coordinates are numbers
    def validate_heading(self, angle):
        if not isinstance(angle, (int, float)):
            raise TypeError("Heading must be a number")
        return angle % 360
    
    # ----------- Pen Movements ------------
    def forward(self, distance):
        rad = math.radians(self._heading)
        #converting heading to radians

        #calculating new coordinates using cos and sin 
        new_x = self._position.x + distance * math.cos(rad)
        new_y = self._position.y - distance * math.sin(rad)  
        new_pos = Point(new_x, new_y)
        
        #draw a new line if pen is down otherwise move function
        if self._pendown:
            self._pen.line_to(new_x, new_y)
        else:
            self._pen.move_to(new_x, new_y)

        self._position = new_pos

    def turn_left(self, angle):
        self._heading = self.validate_heading(self._heading + angle)
    
    def turn_right(self, angle):
        self._heading = self.validate_heading(self._heading - angle)

    # -------- Pen state --------
    def penup(self):
        self._pendown = False
        # Lifts the pen: moves without drawing
    
    def pendown(self):
        self._pendown = True
        #Lowers the pen: moves will draw
    
    def __str__(self):
        return f"Turtle(position={self._position}, heading={self._heading})"