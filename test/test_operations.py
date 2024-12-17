import pytest
from multiply import multiply
from divide import divide

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(-6, 3) == -2

    with pytest.raises(ValueError):
        divide(5, 0)
