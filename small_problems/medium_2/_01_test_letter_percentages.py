from _01_lettercase_percentage_case import letter_percentages

def test_letter_percentages1():
    assert letter_percentages('abCdef 123') == {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}

def test_letter_percentages2():
    assert letter_percentages('AbCd +Ef') == {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}

def test_letter_percentages3():
    assert letter_percentages('123') == {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}