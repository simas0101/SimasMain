from plates import is_valid

def test_starts():
    assert is_valid("CS") == True
    assert is_valid("55") == False
    assert is_valid("5") == False
    assert is_valid("C5") == False

def test_contains():
    assert is_valid("Abcdef") == True
    assert is_valid("Ab") == True
    assert is_valid("Abcdefg") == False

def test_used():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False

def test_zero():
    assert is_valid("ABC01") == False

def test_allowed():
    assert is_valid("CS50") == True
    assert is_valid("CS!50") == False
