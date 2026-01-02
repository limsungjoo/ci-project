# test_app.py
from app import add

def test_add():
    assert add(1, 2) == 3
    assert add(10, 5) == 15
