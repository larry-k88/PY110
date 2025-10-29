from _03_triangles import triangle

def test_triangle():
    assert triangle(60, 70, 50) == "acute"
    assert triangle(30, 90, 60) == "right" 
    assert triangle(120, 50, 10) == "obtuse"
    assert triangle(0, 90, 90) == "invalid"
    assert triangle(50, 50, 50) == "invalid"