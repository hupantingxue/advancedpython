#!/usr/bin/env python
import pdb

if "__main__" == __name__:
    """
      $ python err.py 
      > src/github/advancedpython/pdb/err.py(7)<module>()
      -> print 10 / n
      (Pdb) p n
      0
      (Pdb) c
      Traceback (most recent call last):
        File "err.py", line 20, in <module>
          print 10 / n
      ZeroDivisionError: integer division or modulo by zero
    """
    s = '0'
    n = int(s)
    pdb.set_trace()
    print 10 / n
