import numb3rs
import pytest

def test_true():
    assert numb3rs.validate("1.1.1.1") == True
    assert numb3rs.validate("250.255.3.4") == True

def test_false():
    assert numb3rs.validate("255.267.1.2") == False
    assert numb3rs.validate("cat") == False