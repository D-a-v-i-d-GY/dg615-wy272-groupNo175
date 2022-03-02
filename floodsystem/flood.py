"""This module contains a collection of functions related to
predicting the occurence of flooding.
"""

from floodsystem.station import MonitoringStation


def stations_level_over_threshold(stations, tol):
    """Return all stations with a RELATIVE level greater than a tolerance (tol).
    """

    # Check data consistency
    if not isinstance(stations, list):
        return None
    if not isinstance(tol, float):
        return None
    if len(stations) == 0:
        return None
    if not isinstance(stations[0], MonitoringStation):
        return None
    if not tol > 0:
        return None

    
    return [
        (station, station.relative_water_level()) 
        for station in stations
        if station.relative_water_level() != None 
        and station.relative_water_level() > tol
        ]

def stations_highest_rel_level(stations, N):
    """Returns first N stations with the highest relative water levels.
    """
    # Check data consistency
    if not isinstance(stations, list):
        return None
    if not isinstance(N, int):
        return None
    if len(stations) == 0:
        return None
    if not isinstance(stations[0], MonitoringStation):
        return None
    if N <= 0 or N > len(stations):
        return None

    #Trim stations with bad data
    stations = [station for station in stations if station.relative_water_level() != None]
    #Sort stations by attribute
    stations.sort(
        key=lambda station: station.relative_water_level(),
        reverse=True
        )

    #Splice
    return stations[:N]