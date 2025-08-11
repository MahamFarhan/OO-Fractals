import math
from Geometry.point import Point
from Drawing.canvas import Canvas
class Turtle:
    def __init__(self, start_point, start_angle=0):
       self.x, self.y = start_point.x, start_point.y
       self.angle = start_angle  # Angle in degrees
       self.canvas = None
    def set_canvas(self, canvas):
        self.canvas = canvas
    def forward(self, distance=20):
        rad = math.radians(self.angle)
        new_x = self.x + distance * math.cos(rad)
        new_y = self.y + distance * math.sin(rad)
        if self.canvas:
            self.canvas.add_line(Point(self.x, self.y), Point(new_x, new_y), color="black", width=2, style="solid")
        print(f"Forward to ({new_x:.1f}, {new_y:.1f})")
        self.x, self.y = new_x, new_y
    def turn_left(self, angle=90):
        self.angle = (self.angle + angle) % 360
        print(f"Turn left to {self.angle} degrees")
    def turn_right(self, angle=90):
        self.angle = (self.angle - angle) % 360
        print(f"Turn right to {self.angle} degrees")