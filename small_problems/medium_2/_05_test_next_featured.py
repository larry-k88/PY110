from _05_next_featured import next_featured

def test_next_featured_small():
    assert (next_featured(12) == 21)                
    assert (next_featured(20) == 21)                
    assert (next_featured(21) == 35)

def test_next_featured_medium():        
    assert (next_featured(997) == 1029)             
    assert (next_featured(1029) == 1043)

def test_next_featured_large():  
    assert (next_featured(999999) == 1023547)       
    assert (next_featured(999999987) == 1023456987) 
    assert (next_featured(9876543186) == 9876543201)
    assert (next_featured(9876543200) == 9876543201)

def test_next_featured_error():
    error = ("There is no possible number that "
            "fulfils those requirements.")
    assert (next_featured(9876543201) == error)