import pytest 

from circle import Circle
from rectangle import Rectangle

circle1 = Circle(0, 0, 1)
circle2 = Circle(1, 1, 1)
rectangle = Rectangle(0, 0, 1, 1)

print(circle1 == circle2) # True, same area
print(circle1 == rectangle) # False
circle1.translate(5, 3)
circle3 = Circle(radius=3)
print(circle3 >= circle1) # True

