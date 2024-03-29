from mypackage import myModule
from mypackage import fibModule

def test_top_n():
    """
    Test to make sure top_n works
    """
    assert myModule.top_n([7,9,3,5,1], 3) == [9,7,5], 'incorrect'
    assert myModule.top_n([11,9,43,15,10,23,5], 2) == [43,23], 'incorrect'
    assert myModule.top_n([17,29,33,5,11], 4) == [33,29,17,11], 'incorrect'

def test_fibonacci():
    """
    Test the fibonacci sequence to make sure it works
    """
    assert fibModule.fibonacci(3) == 2, 'incorrect'
    assert fibModule.fibonacci(5) == 5, 'incorrect'
    assert fibModule.fibonacci(6) == 8, 'incorrect'
    