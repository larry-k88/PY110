from _09_staggered_case_2 import staggered_case

def test_staggered_cased_1():
    assert staggered_case(string_1) == result_1

def test_staggered_cased_2():
    assert staggered_case(string_2) == result_2

def test_staggered_cased_3():
    assert staggered_case(string_3) == result_3

def test_staggered_case_empty():
    assert staggered_case('') == ""

string_1 = 'I Love Launch School!'
result_1 = "I lOvE lAuNcH sChOoL!"

string_2 = 'ALL_CAPS'
result_2 = "AlL_cApS"

string_3 = 'ignore 77 the 4444 numbers'
result_3 = "IgNoRe 77 ThE 4444 nUmBeRs"