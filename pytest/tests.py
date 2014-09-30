"""
  pytest sample

  The unittest module comes with a ‘discovery’ option.
  Discovery is just built in to pytest.

  pytest comes with 'discovery' function;
    see also in: http://pytest.org/latest/example/pythoncollection.html

  Run test:
      python -m pytest tests.py -v
"""
from mydict import MyDict

def test_mydict():
    md = MyDict()
    md["k1"] = "v1"
    assert(md["k1"] == "v1")
