import math
class vector2D:
    def __init__(self, dx: float=0.0, dy: float=0.0):
        self._dx = dx
        self._dy = dy
    @classmethod
    def from_angle(cls, angle_radians: float, magnitude: float = 1.0):
        return cls(math.cos(angle_radians) * magnitude, math.sin(angle_radians) * magnitude)

    def __add__(self, other: "vector2D"):
        return vector2D(self._dx + other._dx, self._dy + other._dy)

    def __sub__(self, other: "vector2D"):
        return vector2D(self._dx - other._dx, self._dy - other._dy)

    def scale(self, factor: float):
        return vector2D(self._dx * factor, self._dy * factor)

    def length(self):
        return math.hypot(self._dx, self._dy)

    def normalized(self):
        l = self.length()
        if l == 0:
            return vector2D(0, 0)
        return vector2D(self._dx / l, self._dy / l)

    def rotate(self, angle_radians: float):
        cos_a = math.cos(angle_radians)
        sin_a = math.sin(angle_radians)
        return vector2D(
            self._dx * cos_a - self._dy * sin_a,
            self._dx * sin_a + self._dy * cos_a,
        )

    def to_tuple(self):
        return (self._dx, self._dy)

    def __repr__(self):
        return f"Vector2D(dx={self._dx:.3f}, dy={self._dy:.3f})"