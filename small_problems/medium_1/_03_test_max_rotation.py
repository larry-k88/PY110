from _03_rotation_3 import max_rotation

def test_max_rotation():
    assert max_rotation(735291) == 321579 
    assert max_rotation(3) == 3        
    assert max_rotation(35) == 53
    assert max_rotation(8703529146) == 7321609845

def test_max_rotation_leading_zero():
    assert max_rotation(105) == 15
