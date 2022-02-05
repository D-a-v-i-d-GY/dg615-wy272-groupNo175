# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine

def stations_by_distance(stations, p):
    """For a list of stations (MonitoringStation object) and
    coordinate p (latitude, longitude), returns list of tuples
    (station, distance) sorted by the distance from the given
    coordinate p"""

    # Create the list of (stations, distance) tuples
    station_dist = []

    # Append data to the list
    for station in stations:
        station_dist.append((station, haversine(p, station.coord)))

    # Return station_dist list sorted by the distance from p
    return sorted_by_key(station_dist, 1)


def stations_within_radius(stations, centre, r):
    """For a list of stations (MonitoringStation object),
        centre (latitude, longitude), and radius r (float) returns list of
        stations (MonitoringStation object) within radius r from the
        given centre"""
    
    # Get the sorted list of (station, distance) tuples
    stations_dist = stations_by_distance(stations, centre)

    # Find the index of the furthest station within radius r
    i = 0
    for k in range(len(stations_dist)):
        if stations_dist[k][1] >= r:
            i = k
            break

    # The list is sorted, so return all the entries up to index i.
    # List comprehension is used to drop the distances
    return [station_dist[0] for station_dist in stations_dist[:i]]

def rivers_by_station_number(stations, N):
    """Find the N rivers with the greatest number of monitoring stations"""

    # Collect all rivers
    rivers = [station.river for station in stations]
    
    # Tally across river set and sort by descending count
    sorted_rivers = sorted(
        [(river, rivers.count(river)) for river in set(rivers)],
        key= lambda pair: pair[1],
        reverse= True
    )

    # Get all counts to filter for duplicates
    top_n_counts = set([river[1] for river in sorted_rivers])

    # Filter for only rivers that occur in top N by count
    n_rivers = [river for river in sorted_rivers if river[1] in list(top_n_counts)[-N:]]

    return n_rivers