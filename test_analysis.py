from pyrsistent import v
from floodsystem.analysis import *
from datetime import datetime
import numpy as np

def test_polyfit():
    assert polyfit([],[0.314], 3) == None
    assert polyfit([datetime(2022,1,15,12,13,14)],[], 3) == None
    assert polyfit(5,[0.314], 3) == None
    assert polyfit([datetime(2022,1,15,12,13,14)],5, 3) == None
    assert polyfit([5],[0.314], 3) == None
    assert polyfit([datetime(2022,1,15,12,13,14)],["hello"], 3) == None
    assert polyfit([datetime(2022,1,15,12,13,14)],[0.314], 0) == None
    assert polyfit([datetime(2022,1,15,12,13,14)],[0.314], 1.5) == None
    assert polyfit([datetime(2022,1,15,12,13,14), datetime(2022,1,15,12,13,15)],[0.314, 0.315], 1) != None


def test_first_derivative():
    assert first_derivative("hello", 1.5) == None
    assert first_derivative((np.poly1d([1, 2]), 1.5), "hello") == None
    assert first_derivative((np.poly1d([1, 2]), 1.5, 1.5), 1.5) == None
    assert first_derivative(([1, 2], 1.5), 1.5) == None
    assert first_derivative((np.poly1d([1.0, 2.0]), "hello"), 1.5) == None
    assert first_derivative((np.poly1d([1.0, 1.0, 1.0]), 0.0), 1.0) == 3.0
    assert first_derivative((np.poly1d([1.0, 1.0, 1.0]), 0.0), 0.0) == 1.0
    assert first_derivative((np.poly1d([1.0, 1.0, 1.0]), 1.0), 1.0) == 1.0
    assert first_derivative((np.poly1d([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]), 0.0), 1.0) == 21.0

def test_second_derivative():
    assert second_derivative("hello", 1.5) == None
    assert second_derivative((np.poly1d([1, 2]), 1.5), "hello") == None
    assert second_derivative((np.poly1d([1, 2]), 1.5, 1.5), 1.5) == None
    assert second_derivative(([1, 2], 1.5), 1.5) == None
    assert second_derivative((np.poly1d([1.0, 2.0]), "hello"), 1.5) == None
    assert second_derivative((np.poly1d([1.0, 1.0, 1.0]), 0.0), 1.0) == 2.0
    assert second_derivative((np.poly1d([1.0, 1.0, 1.0]), 0.0), 0.0) == 2.0
    assert second_derivative((np.poly1d([1.0, 1.0, 1.0]), 1.0), 1.0) == 2.0
    assert second_derivative((np.poly1d([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]), 0.0), 1.0) == 70.0