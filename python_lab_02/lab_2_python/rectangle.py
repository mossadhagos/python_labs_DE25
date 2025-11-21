from shape import Shape2D

class Rectangle(Shape2D):
    """
    Definierar en rektangel som en konkret 2D-form med position, bredd och höjd.
    Validerar dimensioner, exponerar geometriska egenskaper och kontrollerar om
    formen är en kvadrat.
    """
    
    def __init__(self, x: float = 0, y: float = 0, width: float = 1, height: float = 1):
        super().__init__(x,y)
        if not isinstance(width, (int, float)) or not isinstance(height,(int, float )):
            raise TypeError("width and height must be numbers")
    
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be postive")
        self.width = float(width)
        self.height = float(height)
    
  
    @property
    def area(self) -> float:
        return self.width * self.height

    @property
    def perimeter(self) -> float:
        return 2 * (self.width * self.height)
    
    def is_square(self) -> bool:
        return self.width == self.height