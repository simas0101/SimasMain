import working
import pytest

def test_convert():
    assert working.convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert working.convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert working.convert("9 PM to 7 AM") == "21:00 to 07:00"
    assert working.convert("11:30 PM to 8:55 AM") == "23:30 to 08:55"
    assert working.convert("10 AM to 9:14 PM") == "10:00 to 21:14"

def test_error():
    with pytest.raises(ValueError):
        working.convert("12:60 AM to 5 PM")
    with pytest.raises(ValueError):
        working.convert("13:00 AM to 8:30 PM")
    with pytest.raises(ValueError):
        working.convert("12:60 AM 5 PM")


