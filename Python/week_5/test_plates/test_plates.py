from plates import is_valid

def test_start_with_letters():
    assert is_valid("AB1234") == True
    assert is_valid("A12345") == False

def test_length():
    assert is_valid("AB") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

def test_number_rules():
    assert is_valid("AB123") == True
    assert is_valid("AB0123") == False
    assert is_valid("ABC12D") == False

def test_no_punctuation():
    assert is_valid("AB1234") == True
    assert is_valid("ABC123!") == False

def test_valid_plates():
    assert is_valid("HELLO") == True
    assert is_valid("CS50") == True
    assert is_valid("GO123") == True
