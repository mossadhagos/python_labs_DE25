# vi importerar math för att få tillgång till PI
# vi impoterar Shape2D klassen
import math
from shape import Shape2D

# skappar Circle kalssen 
class Circle(Shape2D):
    
    # skappar dunder init
    def __init__(self, x: float = 0, y: float = 0, radius: float = 1 ):
        # här hämtar/roppar på instroktioner från huvud klassen Shape2D
        super().__init__(x, y) 
        
        # säker ställer att radius är nummer typen (int eller float)
        if not isinstance(radius, (int, float )):
            raise TypeError ("radius must be a number")
        
        # detta ser till att radius är större än 0 
        if radius <= 0:
            raise ValueError("radius must be positive")
        
        # här förvarar vi radius som float 
        self.radius = float(radius)
        
   
    # formel för arean av circkel A = pi * r **2
    @property
    def area(self) -> float:
        return math.pi * self.radius**2
    
    # formel för omkräts av circkel c = 2 * pi *r
    @property
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius
    
    # detta ger (returns) radius är exakt 1 (a unit circle)
    def is_unit(self) -> bool:
        return self.radius == 1