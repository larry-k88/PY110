from _10_remove_consecutive_duplicates import unique_sequence

def test_unique_sequence():
    assert unique_sequence(original_1) == expected_1
    assert unique_sequence(original_2) == expected_2

original_1 = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected_1 = [1, 2, 6, 5, 3, 4]

original_2 = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4, 6]
expected_2 = [1, 2, 6, 5, 3, 4, 6]