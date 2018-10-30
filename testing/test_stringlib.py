import pytest
from testing.stringlib import *

def test_lettercount_basic1():
    assert(letterCount("hi", "i") == 1)

def test_lettercount_basic2():
    assert(letterCount("heyyo buddy", "y") == 3)

def test_lettercount_emptyletter():
    assert(letterCount("pop goes the weasel", "") == 0)

def test_lettercount_emptystr():
    assert(letterCount("", "o") == 0)

def test_lettercount_empty():
    assert(letterCount("", "") == 0)

def test_removeSpace_basic1():
    assert(removeSpace("Hey everybody!") == "Heyeverybody!")

def test_removeSpace_basic2():
    assert(removeSpace("Hi!    hi") == "Hi!hi")

def test_removeSpace_emptySpace():
    assert(removeSpace("  ") == "")

def test_removeSpace_emptyStr():
    assert(removeSpace("") == "")