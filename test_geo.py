""" Unit test for Geo module"""

from distutils.command.build import build
from floodsystem.station import build_station_list
import floodsystem.geo as geo

# Task 1E
def test_rivers_by_station_number():
    stations = build_station_list()
    N = 10
    n_rivers = geo.rivers_by_station_number(stations, N)

    # Check that the returned list is not empty and does not exceed total
    assert len(n_rivers) > 0 and len(n_rivers) < len(stations)

    # Check that the returned list is sorted correctly
    assert sorted(n_rivers, reverse=True) == n_rivers

