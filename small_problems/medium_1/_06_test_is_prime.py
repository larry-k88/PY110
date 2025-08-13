from _06_is_it_prime import is_prime

def test_is_prime_true():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(23) == True
    assert is_prime(997) == True
    assert is_prime(3_297_061) == True


def test_is_prime_false():
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False
    assert is_prime(24) == False
    assert is_prime(998) == False
    assert is_prime(23_297_061) == False