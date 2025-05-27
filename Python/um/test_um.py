import um
import pytest

def test_count():
    assert um.count("um") == 1
    assert um.count("hello, um, world") == 1
    assert um.count("Um, thanks, um...") == 2
    assert um.count("yummy") == 0