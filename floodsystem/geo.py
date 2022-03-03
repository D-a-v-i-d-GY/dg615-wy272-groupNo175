# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.utils import sorted_by_key  # noqa
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
    # Validate Entry
    if r <= 0:
        print("Radius must be positive.")
        return False

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


def rivers_with_station(stations):
    """Given list of stations (MonitoringStation object), return the
    names of the rivers that are being monitored"""

    # Collect all the names of the rivers in a set to avoid duplicate entries
    rivers = {station.river for station in stations}

    # Return a list for convenience
    return list(rivers)


def stations_by_river(stations, names=True):
    """Given list of stations (MonitoringStation object), return a
    dictionary that has names of the rivers as keys and list of the
    names of the stations that monitor that river as values"""
    # Get the names of the rivers
    rivers = rivers_with_station(stations)

    # Initialize the dictionary with the river names as keys and empty lists as values
    river_dict = {river: [] for river in rivers}

    # Update the dicionary by appending the names of the stations to the corresponding lists
    if names:
        for station in stations:
            river_dict[station.river].append(station.name)
    else:
        for station in stations:
                    river_dict[station.river].append(station)
    # Return the produced dictionary
    return river_dict


def rivers_by_station_number(stations, N):
    """Find the N rivers with the greatest number of monitoring stations"""

    # Validate input
    if type(N) is not int or N <= 0:
        print("Invalid N.")
        return False

    # Collect all rivers
    rivers = [station.river for station in stations]
    
    # Tally across river set and sort by descending count (eliminate duplicates)
    sorted_rivers = sorted(
        [(river, rivers.count(river)) for river in set(rivers)],
        key= lambda pair: pair[1],
        reverse= True
    )

    # Get all tallies and filter for duplicates
    tallies = {river[1] for river in sorted_rivers}

    # Check that N does not exceed number of rivers found
    if N > len(tallies):
        print("There are less than N rivers.")
        return False

    # Filter for only rivers that occur in top N by count
    n_rivers = [river for river in sorted_rivers if river[1] in list(tallies)[-N:]]

    return n_rivers


def towns_with_station(stations):
    """Given list of stations (MonitoringStation object), return the
    names of the towns that have monitoring stations"""

    # Collect all the names of the towns in a set to avoid duplicate entries
    towns = {station.town for station in stations if station.town is not None}

    # Return a list for convenience
    return list(towns)


def stations_by_towns(stations):
    """Given list of stations (MonitoringStation object), return a
    dictionary that has names of the towns as keys and list of the
    names of the stations that are in that town as values"""

    # Get the names of the towns
    towns = towns_with_station(stations)

    # Initialize the dictionary with the town names as keys and empty lists as values
    town_dict = {town: [] for town in towns}

    # Update the dicionary by appending the names of the stations to the corresponding lists
    for station in stations:
        if station.town is not None:
            town_dict[station.town].append(station)

    # Return the produced dictionary
    return town_dict