import pytest
from jar import Jar

def test_initialization():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0

    with pytest.raises(ValueError):
        jar = Jar(-5)

def test_deposit():
    jar = Jar(10)
    jar.deposit(3)
    assert jar.size == 3
    assert str(jar) == "🍪🍪🍪"

    with pytest.raises(ValueError):
        jar.deposit(8)

def test_withdraw():
    jar = Jar(10)
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3
    assert str(jar) == "🍪🍪🍪"

    with pytest.raises(ValueError):
        jar.withdraw(4)

def test_str_representation():
    jar = Jar(5)
    jar.deposit(2)
    assert str(jar) == "🍪🍪"

    jar.deposit(1)
    assert str(jar) == "🍪🍪🍪"

def test_full_capacity():
    jar = Jar(3)
    jar.deposit(3)
    assert jar.size == 3
    assert str(jar) == "🍪🍪🍪"

    with pytest.raises(ValueError):
        jar.deposit(1)
