#!/usr/bin/env  python
#-*- coding: utf-8 -*-

"""
    The standard workflow is:
  1. You define your own class derived from unittest.TestCase.
  2. Then you fill it with functions that start with ‘test_’.
  3. You run the tests by placing unittest.main() in your file, usually at the bottom. 
"""

import unittest
from mydict import *

class MyDictTest(unittest.TestCase):
    """ mydict unit test case.

    How to run?
        1).  python mydict_test.py 
        2).  python -m unittest mydict_test  # without (.py)

    Run Result:
        ...
        ----------------------------------------------------------------------
        Ran 3 tests in 0.000s
        
        OK
    """
    def test_init(self):
        d1 = MyDict(k1="v1", k2=2)
        self.assertEquals(d1["k1"], "v1")
        self.assertEquals(d1["k2"], 2)
        self.assertTrue(isinstance(d1, dict))

    def test_getatrr(self):
        d1 = MyDict(a=1)
        self.assertEquals(d1["a"], 1)

    def test_setattr(self):
        d1 = MyDict(a=1)
        d1["a"] = 2
        self.assertEquals(d1["a"], 2)

if "__main__" == __name__:
    unittest.main()
