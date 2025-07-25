from _03_delete_vowels import remove_vowels

def test_remove_vowels_1():
    assert remove_vowels(original_1) == expected_1

original_1 = ['abcdefghijklmnopqrstuvwxyz']
expected_1 = ['bcdfghjklmnpqrstvwxyz']

def test_remove_vowels_2():
    assert remove_vowels(original_2) == expected_2

original_2 = ['green', 'YELLOW', 'black', 'white']
expected_2 = ['grn', 'YLLW', 'blck', 'wht']

def test_remove_vowels_3():
    assert remove_vowels(original_3) == expected_3

original_3 = ['ABC', 'AEIOU', 'XYZ']
expected_3 = ['BC', '', 'XYZ']
