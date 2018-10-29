import pytest
from stringlib import *

def test_lettercount_basic1():
    assert (lettercount("hi") == 2)

def test_lettercount_basic2():
    assert (lettercount("fight me") == 8)

def test_lettercount_empty():
    assert (lettercount("") == 0)


