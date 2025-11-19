# Changed the format of the tests to call the function, then assert
# that the object itself is as expected (rather than the return value
# of calling the function on the object, which is None)
from _07_bubble_sort import bubble_sort

def test_bubble_sort_1():
    lst1 = [5, 3]
    bubble_sort(lst1)
    assert lst1 == [3, 5]

def test_bubble_sort_2():
    lst2 = [6, 2, 7, 1, 4]
    bubble_sort(lst2)
    assert lst2 == [1, 2, 4, 6, 7]

def test_bubble_sort_3():
    lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
            'Kim', 'Bonnie']
    bubble_sort(lst3)
    assert lst3 == ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]