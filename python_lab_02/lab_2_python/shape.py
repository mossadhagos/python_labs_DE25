from abc import ABC, abstractmethod

class Shape2D (ABC):
    """Abstrakt 2D-form med position, translation,
    krav på area och omkrets i subklasser samt jämförelse- och strängrepresentation
    baserad på formens egenskaper.""" 
    
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = float(x)
        self.y = float(y)
        
    def translate(self, dx: float, dy: float):
        if not isinstance(dx, (int, float)) or not isinstance(dy, (int, float)):
            raise TypeError("translate() expects numeric values")
        self.x += dx
        self.y += dy
        
    @property
    @abstractmethod
    def area(self) -> float:
        pass
    
    @property
    @abstractmethod
    def perimeter(self) -> float:
        pass
    
    def __eq__(self, other):
        return isinstance(other, Shape2D) and self.area == other.area
 
    def __lt__(self, other):
        return self.area < other.area 
   
    def __le__(self, other):
        return self.area <= other.area
 
    def __gt__(self, other):
        return self.area >= other.area 
    
    def __reper__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"

    def __str__(self):
        return f"{self.__class__.__name__} centered at ({self.x}, {self.y})"