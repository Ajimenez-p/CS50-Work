from um import count

def test_default():
    assert count('') == 0

def test_um_alone():
    assert count('um um um') == 3
    assert count('um um') == 2
    assert count('um, um, UM!') == 3


def test_um_together():
    assert count('yummy! yummers, yum!') == 0
    assert count('yuma, puma, tuma') == 0
