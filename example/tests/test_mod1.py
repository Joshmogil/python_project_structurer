from subpack.mod1 import mycube
from subpack.mod2 import myOtherCube

def test_mycube():
    print(mycube(3))
    assert mycube(3) == 27

def test_myOtherCube():
    print(myOtherCube(3))
    assert myOtherCube(9) == 729 