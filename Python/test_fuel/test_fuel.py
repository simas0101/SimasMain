import fuel
import pytest

def test_convert():
    assert fuel.convert("1/2") == 50
    assert fuel.convert("99/100") == 99
    assert fuel.convert("1/100") == 1

def test_gauge():
    assert fuel.gauge(50) == "50%"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(1) == "E"

def test_Error():
    with pytest.raises(ValueError):
        fuel.convert("6/3")
    with pytest.raises(ZeroDivisionError):
        fuel.convert("5/0")

