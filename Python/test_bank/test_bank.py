from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello, world") == 0

def test_h():
    assert value("Hey") == 20
    assert value("How you doing?") == 20

def test_other():
    assert value("What is happening?") == 100
    assert value("") == 100
