import math 
from shape import Shape2D

class Circle(Shape2D):
    
    def __init__(self, x: float = 0, y: float = 0, radius: float = 1 ):
        super().__init__(x, y) 
        
        if not isinstance(radius, (int, float )):
            raise TypeError ("radius must be a number")
        
        if radius <= 0:
            raise ValueError("radius must be positive")
        self.radius = float(radius)
        
    
    @property
    def area(self) -> float:
        return math.pi * self.radius**2
    
    @property
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius
    
    def is_unit(self) -> bool:
        return self.radius == 1