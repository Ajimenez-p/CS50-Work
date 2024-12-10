from bank import value

#4 tests: if default (no greeting)
def test_default():
    assert value('') == 100

#if starts with hello
def test_starts_with_hello():
    assert value('hello how are you') == 0
    assert value('hello') == 0

#if start with h
def test_starts_with_h():
    assert value('hey') == 20
    assert value('hi how why hn') == 20

#if start with anything other than h
def test_starts_with_other():
    assert value('melon') == 100
    assert value('100') == 100
