from floodsystem.analysis import *
from datetime import datetime

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