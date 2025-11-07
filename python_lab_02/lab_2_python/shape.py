# jag importerar värktyg jaga behöver 
# ABC = abstract base class support
# abstractmethod låter oss decklerar medtoder som måste bli "overridden" i sub klasser 

from abc import ABC, abstractmethod

# detta klass är abstract och kan inte bli instantiatad 
class Shape2D (ABC):
    
    # vi måste ha en dunder init 
    def __init__(self, x: float = 0.0, y: float = 0.0):
        
        # vi sätter positioner av shpe (x, y)
        # vi säker ställer att värden är förvarade som float 
        self.x = float(x)
        self.y = float(y)
        
    # här säker ställer vi att värdena är nummer 
    def translate(self, dx: float, dy: float):
        if not isinstance(dx, (int, float)) or not isinstance(dy, (int, float)):
            raise TypeError("translate() expects numeric values")
         # här lägger vi till dx och dy till de nuvarde postion 
        self.x += dx
        self.y += dy
       
       
    # här är en abstract property och sub klasser måste implemntera detta    
    @property
    @abstractmethod
    def area(self) -> float:
        pass
    
    
    @property
    @abstractmethod
    def perimeter(self) -> float:
        pass
    
    # kolla om cirkel och rectangle har samma area
    def __eq__(self, other):
        return isinstance(other, Shape2D) and self.area == other.area 
    
    # mider än jämförelse baserad på area 
    def __lt__(self, other):
        return self.area < other.area 
    
    # mer än jämförelse 
    def __le__(self, other):
        return self.area <= other.area
    
    # störe än eller lika med jämföreslse 
    def __gt__(self, other):
        return self.area >= other.area 
    
    # en string represtation för debugging 
    def __reper__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"
    
    # och här är en avändar vänlig string repistation 
    def __str__(self):
        return f"{self.__class__.__name__} centered at ({self.x}, {self.y})"