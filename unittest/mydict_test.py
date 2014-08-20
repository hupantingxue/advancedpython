#!/usr/bin/env  python
#-*- coding: utf-8 -*-

import unittest
from mydict import *

class MyDictTest(unittest.TestCase):
    """
        pass
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
