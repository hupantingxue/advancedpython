#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Parrot(object):
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        """Get the current voltage"""
        return self._voltage

    @voltage.setter
    def voltage(self, value):
        """Set the voltage"""
        if not isinstance(value, int):
            raise ValueError('voltage must be integer')
        if 0 > value or 9999999 < value:
            raise ValueError('voltage must between 0~9999999')
        self._voltage = value

    @voltage.deleter
    def voltage(self):
        """Del the voltage"""
        del self._voltage
