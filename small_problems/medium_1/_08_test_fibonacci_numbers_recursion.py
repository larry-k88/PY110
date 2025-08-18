from _08_fibonacci_numbers_recursion import fibonacci

def test_fibonacci():
    assert fibonacci(1) == 1 
    assert fibonacci(2) == 1 
    assert fibonacci(3) == 2 
    assert fibonacci(4) == 3 
    assert fibonacci(5) == 5 
    assert fibonacci(6) == 8
    assert fibonacci(12) == 144
    assert fibonacci(20) == 6765