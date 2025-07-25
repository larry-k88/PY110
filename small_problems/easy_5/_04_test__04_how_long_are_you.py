from _04_how_long_are_you import word_lengths

def test_word_lengths_1():
    assert word_lengths(words_1) == ['cow 3', 'sheep 5', 'chicken 7']

def test_word_lengths_2():
    assert word_lengths(words_2) == ['baseball 8', 'hot 3', 'dogs 4',
                   'and 3', 'apple 5', 'pie 3']

def test_word_lengths_3():
    assert word_lengths(words_3) == ['It 2', "ain't 5", 'easy, 5',
                   'is 2', 'it? 3']

def test_word_lengths_4():
    assert word_lengths(big_word) == [f'{big_word} 34']

def test_word_lengths_empty():
    assert word_lengths('') == []
    assert word_lengths() == []
    assert word_lengths(None) == []
    assert word_lengths({}) == []
    assert word_lengths([]) == []

words_1 = 'cow sheep chicken'
words_2 = 'baseball hot dogs and apple pie'
words_3 = "It ain't easy, is it?"
big_word = 'Supercalifragilisticexpialidocious'