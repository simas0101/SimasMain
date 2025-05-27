import pytest
from datetime import date
from seasons import get_date

def test_get_date():
    assert get_date("1999-01-01").date == date(1999, 1, 1)
    assert get_date("2022-12-14").date == date(2022, 12, 14)

def test_error():
    with pytest.raises(ValueError):
        get_date("January 1, 1999")
