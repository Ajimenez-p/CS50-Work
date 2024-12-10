"""
Then, in a file called test_twttr.py, implement one or more functions that collectively test your
implementation of shorten thoroughly, each of whose names should begin with test_ so
that you can execute your tests with:
"""
from twttr import shorten
#the way the function is built, inputting numbers wont harm the function
#due to this, we can test the actual STR itself
#we will test  UPPERCASE, lowercase,             spaces            , and the absence of input
def test_uppercase():
    assert shorten('UPPERCASE') == 'PPRCS'


def test_lowercase():
    assert shorten('lowercase') == 'lwrcs'


def test_default():
    assert shorten('') == ''
