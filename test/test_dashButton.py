import pytest
import os
from src.dashbutton import dashButton

def test_pass():
    pass

def test_readCSV_invalid_file():
    assert dashButton.readCSV("fakeFile.txt") == 1

def test_readCSV_valid_file():
    pathToExample = os.path.join(os.getcwd(), "test/example.csv")
    dashButton.readCSV(pathToExample)
    assert len(dashButton.buttonDict) == 1
    assert "fakeButton" in dashButton.buttonDict.keys()
    assert "00:22:33:44" in dashButton.buttonDict.values()
