import pytest
from working import convert

def test_valid_input():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"
    assert convert("1:00 PM to 11:59 PM") == "13:00 to 23:59"

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("12:00 to 13:00 PM")

def test_edge_cases():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"
