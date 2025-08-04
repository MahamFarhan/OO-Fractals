from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self, color="black", width=1):
        self._color = color
        self._width = width
    @property
    def color(self):
        return self._color
    @property
    def width(self):
        return self._width
    @abstractmethod
    def draw(self, pen):
        pass
    def __str__(self):
        return f"{self.__class__.__name__}(color={self.color}, width={self.width})"

    def __repr__(self):
        return str(self)