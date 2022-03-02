# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains utility functions.

"""
from floodsystem.station import MonitoringStation

def sorted_by_key(x, i, reverse=False):
    """For a list of lists/tuples, return list sorted by the ith
    component of the list/tuple, E.g.

    Sort on first entry of tuple:

      > sorted_by_key([(1, 2), (5, 1]), 0)
      >>> [(1, 2), (5, 1)]

    Sort on second entry of tuple:

      > sorted_by_key([(1, 2), (5, 1]), 1)
      >>> [(5, 1), (1, 2)]

    """

    # Sort by distance
    def key(element):
        return element[i]

    return sorted(x, key=key, reverse=reverse)

def id_station(stations, name):
  # Check data consistency
    if not isinstance(stations, list):
        return None
    if not isinstance(name, str):
        return None
    if len(stations) == 0:
        return None
    if not isinstance(stations[0], MonitoringStation):
        return None

    for station in stations:
        if station.name == name:
            print(station)
            print(station.latest_level)
            print(station.relative_water_level())