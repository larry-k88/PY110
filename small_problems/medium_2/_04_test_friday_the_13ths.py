from _04_unlucky_days import friday_the_13ths

def test_friday_the_13ths():
    assert friday_the_13ths(1986) == 1
    assert friday_the_13ths(2015) == 3
    assert friday_the_13ths(2017) == 2