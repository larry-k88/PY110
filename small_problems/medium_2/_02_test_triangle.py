from _02_triangle_sides import triangle

def test_triangle():
    assert triangle(3, 3, 3) == "equilateral"
    assert triangle(3, 3, 1.5) == "isosceles"
    assert triangle(3, 4, 5) == "scalene"
    assert triangle(0, 3, 3) == "invalid"
    assert triangle(3, 1, 1) == "invalid"

def test_triangle_extra():
    assert triangle(2, 2, 4) == 'invalid'
    assert triangle(-1, 3, 3) == 'invalid'
    assert triangle(2, 3, 3) == 'isosceles'
    assert triangle(3, 4, 5) == 'scalene'