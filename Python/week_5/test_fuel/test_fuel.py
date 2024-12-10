from fuel import convert, gauge
import pytest

def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("99/100") == 99
    assert convert("1/100") == 1
    assert convert("100/100") == 100

def test_convert_invalid():
    with pytest.raises(ValueError):
        convert("2/1")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("hello/world")

def test_gauge_e():
    assert gauge(1) == "E"
    assert gauge(0) == "E"

def test_gauge_f():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_gauge_percentage():
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
    assert gauge(20) == "20%"
