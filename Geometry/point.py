class Point:
    count = 0  # Track number of instances

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y
        Point.count += 1

    @property
    def x(self):
        return self._x
    #@property turns this method into a getter.Now we can do p.x instead of p.get_x().
    @x.setter
    def x(self, value):
        self._x = value
    #Allows p.x = 5 while still keeping _x protected inside.
    
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, value):
        self._y = value

    def translate(self, dx=0, dy=0):
        #Return a new Point moved by dx, dy.
        return Point(self._x + dx, self._y + dy)
        #It creates and returns a new point at the shifted coordinates.
        # This is called immutability the original stays unchanged.

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self._x + other._x, self._y + other._y)
        raise TypeError("Can only add Point to Point")

    def __eq__(self, other):
        return isinstance(other, Point) and self._x == other._x and self._y == other._y

    def distance(self, p):
        #Distance between this point and another.
        return ((self._x - p._x)**2 + (self._y - p._y)**2)**0.5
    def as_tuple(self):
        #Return coordinates as a tuple.
        return (self._x, self._y)

    def __str__(self):
        return f"({self._x}, {self._y})"

    def __repr__(self):
        return f"Point(x={self._x}, y={self._y})"

    @classmethod
    def get_instance_count(cls):
        return cls.count