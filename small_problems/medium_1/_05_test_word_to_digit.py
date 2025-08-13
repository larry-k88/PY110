from _05_word_to_digit import word_to_digit, word_to_digit_2

def test_word_to_digit():
    message = 'Please call me at five five five one two three four'
    assert word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4"

def test_word_to_digit_2():
    message = 'Please call me at five, five, five, one, two, three, four.'
    assert word_to_digit_2(message) == "Please call me at 5, 5, 5, 1, 2, 3, 4."