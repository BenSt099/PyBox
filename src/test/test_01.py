import sys
import pytest
 
sys.path.append('../src/')

from main.PyBox import *

def test_0101():
    box = PyBox()
    assert box.isPresent() == False

def test_0102():
    box = PyBox()
    box.put("test")
    assert box.isPresent() == True
    
def test_0103():
    box = PyBox()
    box.put(None)
    assert box.isPresent() == False
    
def test_0104():
    box = PyBox()
    assert box.isPresent() == False
    
def test_0105():
    box = PyBox()
    box.put("test")
    assert box.get() == "test"
    
def test_0106():
    box = PyBox()
    with pytest.raises(ValueError):
        box.getOrElseThrow(ValueError, "exception raised")