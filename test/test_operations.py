from app.multiply import multiply
from app.divide import divide

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 10) == 0

def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(10, 0)
