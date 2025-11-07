import math
import pytest
from circle import Circle
from rectangle import Rectangle

# Circle tests
def test_circle_area():
    c = Circle(radius=1)
    assert math.isclose(c.area, math.pi, rel_tol=1e-5)

def test_circle_perimeter():
    c = Circle(radius=1)
    assert math.isclose(c.perimeter, 2 * math.pi, rel_tol=1e-5)

def test_circle_translate():
    c = Circle(0, 0, 1)
    c.translate(3, 4)
    assert c.x == 3 and c.y == 4

def test_circle_invalid_radius():
    with pytest.raises(ValueError):
        Circle(radius=-1)

# Rectangle tests
def test_rectangle_area():
    r = Rectangle(width=4, height=5)
    assert r.area == 20

def test_rectangle_is_square():
    r = Rectangle(width=4, height=4)
    assert r.is_square() is True

def test_rectangle_translate():
    r = Rectangle(0, 0, 2, 3)
    r.translate(5, -2)
    assert r.x == 5 and r.y == -2
