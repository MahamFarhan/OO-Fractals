from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self,outline = "black", width=1):
         self._outline = outline
         self._width = width

    @property
    def outline(self):
        return self._outline
    
    @property
    def width(self):
        return self._width

    @abstractmethod
    def draw(self, pen):
        pass

    def __str__(self):
        return f"{self.__class__.__name__}(outline={self.outline}, width={self.width})"

    def __repr__(self):
        return str(self)