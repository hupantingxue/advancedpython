#!/usr/bin/env python
#-*- coding:utf-8 -*-
from parrot import Parrot

if "__main__" == __name__:
    p1 = Parrot()
    print p1.voltage
    p1.voltage = 39
    print p1.voltage
    p1.voltage = -3
    p1.voltage = "33"
