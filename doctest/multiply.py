"""
Module showing how doctests can be included with source code
Each '>>>' line is run as if in a python shell, and counts as a test.
The next line, if not '>>>' is the expected output of the previous line.
If anything doesn't match exactly (including trailing spaces), the test fails.

Run example:
    python -m doctest multiply.py -v  
"""

def multiply(a, b):
    """
    >>> multiply(3, 4)
    12
    >>> multiply(1, 0)
    0
    """
    return (a*b)
