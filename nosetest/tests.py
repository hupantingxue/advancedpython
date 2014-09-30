"""
    A basic test file for nose is pretty simple, without any boilerplate code, without required classes to drive from, without unnecessary imports, and without any extra api.
"""
from add import add

def test_add():
    "Test add function"
    assert(add(3,4) == 7)
