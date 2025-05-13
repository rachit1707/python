from calculator import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16
    assert square(0) == 0

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9
      
