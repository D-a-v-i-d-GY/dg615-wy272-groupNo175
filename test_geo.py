""" Unit test for Geo module"""

from floodsystem.stationdata import build_station_list
import floodsystem.geo as geo

# Task 1D
def test_rivers_with_station():
    stations = build_station_list()

    monitored_rivers = geo.rivers_with_station(stations)
    
    # Check that number of rivers does not exceed total
    assert len(monitored_rivers) <= len(stations)

def test_stations_by_river():
    stations = build_station_list()
    
    # Check that sum of stations by river = total stations
    river_dict = geo.stations_by_river(stations)
    assert len(stations) == sum([len(rivers) for rivers in river_dict.values()])
    

# Task 1E
def test_rivers_by_station_number():
    stations = build_station_list()

    # Check that N is validated
    N = -1
    assert not geo.rivers_by_station_number(stations, N)
    N = 0
    assert not geo.rivers_by_station_number(stations, N)
    N = "sus"
    assert not geo.rivers_by_station_number(stations, N)

    # Check that the returned list is not empty and does not exceed total
    N = 10
    n_rivers = geo.rivers_by_station_number(stations, N)
    assert len(n_rivers) > 0 and len(n_rivers) <= len(stations)

    # Check that the returned list is sorted correctly
    assert sorted(n_rivers, reverse=True, key = lambda x: x[1]) == n_rivers

    