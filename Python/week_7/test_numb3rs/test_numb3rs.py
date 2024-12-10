import pytest
from numb3rs import validate

def test_dot_decimal_format():
    assert validate("192.168.1.1") == True
    assert validate("255.255.255.0") == True
    assert validate("1.1.1.1") == True
    assert validate("0.0.0.0") == True
    assert validate("256.256.256.256") == False
    assert validate("192.168.1") == False
    assert validate("192.168.1.1.1") == False
    assert validate("192.168.1..1") == False
    assert validate("192.168..1") == False
    assert validate("192.168.01.1") == False

def test_range_limits():
    assert validate("-1.168.1.1") == False
    assert validate("192.-168.1.1") == False
    assert validate("192.168.300.1") == False
    assert validate("192.168.1.256") == False
    assert validate("192.168.1.-5") == False
    assert validate("192.168.0.255") == True
    assert validate("0.0.0.255") == True
