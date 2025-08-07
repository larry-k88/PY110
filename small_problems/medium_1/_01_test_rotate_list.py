from _01_rotation_1 import rotate_list

def test_rotate_list():
    assert rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7]
    assert rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a']
    assert rotate_list(['a']) == ['a']
    assert rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1]
    assert rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}]

def test_rotate_list_empty():
    assert rotate_list([]) == []

def test_rotate_list_not_list():
    assert rotate_list(None) == None
    assert rotate_list(1) == None

def test_rotate_list_proof():
    lst = [1, 2, 3, 4]
    assert rotate_list(lst) == [2, 3, 4, 1]
    print(lst == [1, 2, 3, 4])