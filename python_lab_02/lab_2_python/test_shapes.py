# impoterar dem nödvändiga värktygen
# vi impoterar även klasserna vi ska testa 

import math
import pytest
from circle import Circle
from rectangle import Rectangle

# =============
# Circle tests
# =============

# här testar vi arean 
def test_circle_area():
    
    # skappar test med radius = 1
    c = Circle(radius=1)
    # variferar  arean = pi * r **2 -> pi * 1 **2 = pi
    # här anvönder math.isclose för att floating point är inte alltid exakt 
    assert math.isclose(c.area, math.pi, rel_tol=1e-5)

# testar parimeter  
def test_circle_perimeter():
    
    # skappar circle med radius = 1
    c = Circle(radius=1)
    # variferar parimeter (omkräts) = 2 pi r -> 2 pi * 1
    assert math.isclose(c.perimeter, 2 * math.pi, rel_tol=1e-5)


def test_circle_translate():
    
    # skappar  en circle centrerad på (0, 0) med radius = 1
    c = Circle(0, 0, 1)
    # flytta circle med (3,4)
    c.translate(3, 4)
    # kolla att nya kordinaterna updaterats på rätt sätt
    assert c.x == 3 and c.y == 4

def test_circle_invalid_radius():
    # förvänta om radius är negativ 
    # pytest.raises variferar att ValueError kommer upp som förväntat 
    with pytest.raises(ValueError):
        Circle(radius=-1)

# =================
# Rectangle tests
# =================

def test_rectangle_area():
    # skappa rectangle med width = 4 och height = 5
    r = Rectangle(width=4, height=5)
    # area = width * heigth -> 4 * 5 = 20 
    assert r.area == 20

def test_rectangle_is_square():
    # kappar rectangle där width == heigth (en kvadrat)
    r = Rectangle(width=4, height=4)
    # detta borde ge True 
    assert r.is_square() is True

def test_rectangle_translate():
    # rectangle centrerad på (0, 0) med width 2 och height 3
    r = Rectangle(0, 0, 2, 3)
    # flyta rectangle med (5, -2)
    r.translate(5, -2)
    # variferar att den nya positionen är uppdaterad på rätt sätt
    assert r.x == 5 and r.y == -2
