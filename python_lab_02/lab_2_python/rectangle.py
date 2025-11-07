# jag impoterar abstract klassen Shape2D
from shape import Shape2D

# jag skappar klassen rectangle
class Rectangle(Shape2D):
    
    # här har vi en dudder init
    # med klass beskrinving 
    def __init__(self, x: float = 0, y: float = 0, width: float = 1, height: float = 1):
       
       # här hämtar/roppar på instroktioner från huvud klassen Shape2D
        super().__init__(x,y)
        
        # här varifierar vi att bredden och höjden är nummer 
        if not isinstance(width, (int, float)) or not isinstance(height,(int, float )):
            raise TypeError("width and height must be positive")
       
       # här säger vi till att både höjden och bredden är större än 0
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be postive")
        
        # förvarar höjd och bredd som float
        self.width = float(width)
        self.height = float(height)
    
   # detta räknar arean av rectangle A = width * height
    @property
    def area(self) -> float:
        return self.width * self.height
    
   # detta räknar perimeter p = 2 * (width + height)
    @property
    def perimeter(self) -> float:
        return 2 * (self.width * self.height)
    
   # detta svarar True om höjd och bred är samma, och False om det inte är samma 
    def is_square(self) -> bool:
        return self.width == self.height