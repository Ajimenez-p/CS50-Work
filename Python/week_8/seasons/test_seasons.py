import pytest
from seasons import Date

def test_valid_date():
    birth_date = Date('1990-01-01')
    today = Date('2024-01-01')
    assert today.minutes_since(birth_date) == (34 * 365 + 8) * 24 * 60  # 34 years with 8 leap days

def test_leap_year():
    birth_date = Date('2000-02-29')
    today = Date('2024-03-01')
    assert today.minutes_since(birth_date) == (24 * 365 + 6) * 24 * 60 + (24 * 60)  # 24 years with 6 leap days, plus 1 day

def test_invalid_date_format():
    with pytest.raises(ValueError):
        Date('1990-31-12')

def test_today_equals_birthdate():
    birth_date = Date('2024-01-01')
    today = Date('2024-01-01')
    assert today.minutes_since(birth_date) == 0
