from evenodd import even_odd

def test_even_no():
    assert even_odd(10) == "even"

def test_odd_no():
    assert even_odd(7)  == "odd"