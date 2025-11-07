import math
import pytest
from circle import Circle
from rectangle import Rectangle

# -------- Circle tester --------

def test_circle_area():
    c = Circle(radius=1)
    assert math.isclose(c.area, math.pi, rel_tol=1e-5)

def test_circle_perimeter():
    c = Circle(radius=1)
    assert math.isclose(c.perimeter, 2 * math.pi, rel_tol=1e-5)

def test_circle_translate():
    c = Circle(0, 0, 1)
    c.translate(3, 4)
    assert c.x == 3
    assert c.y == 4

def test_circle_invalid_radius_type():
    with pytest.raises(TypeError):
        Circle(radius="hej")

def test_circle_negative_radius():
    with pytest.raises(ValueError):
        Circle(radius=-1)

def test_circle_is_unit():
    assert Circle(radius=1).is_unit() is True
    assert Circle(radius=2).is_unit() is False


# -------- Rectangle tester --------

def test_rectangle_area():
    r = Rectangle(width=4, height=5)
    assert r.area == 20

def test_rectangle_perimeter():
    r = Rectangle(width=4, height=5)
    assert r.perimeter == 18

def test_rectangle_translate():
    r = Rectangle(0, 0, 2, 3)
    r.translate(5, -2)
    assert r.x == 5
    assert r.y == -2

def test_rectangle_invalid_dimensions_type():
    with pytest.raises(TypeError):
        Rectangle(width="hej", height=4)

def test_rectangle_negative_dimensions():
    with pytest.raises(ValueError):
        Rectangle(width=-2, height=3)

def test_rectangle_is_square():
    assert Rectangle(width=4, height=4).is_square() is True
    assert Rectangle(width=4, height=5).is_square() is False

# -------- Shape comparison --------

def test_shape_comparison():
    c = Circle(radius=1)          # area = π
    r = Rectangle(width=2, height=2)  # area = 4
    assert c < r     # π < 4
