from mydict import MyDict

def test_mydict():
    md = MyDict()
    md["k1"] = "v1"
    assert(md["k1"] == "v1")
