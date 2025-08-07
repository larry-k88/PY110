from _02_rotation_2 import rotate_rightmost_digits

def test_rotate_rightmost_digits():
    assert rotate_rightmost_digits(735291, 2) == 735219
    assert rotate_rightmost_digits(735291, 3) == 735912
    assert rotate_rightmost_digits(735291, 1) == 735291
    assert rotate_rightmost_digits(735291, 4) == 732915
    assert rotate_rightmost_digits(735291, 5) == 752913
    assert rotate_rightmost_digits(735291, 6) == 352917
    assert rotate_rightmost_digits(1200, 3) == 1002   