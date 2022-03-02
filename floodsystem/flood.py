"""This module contains a collection of functions related to
predicting the occurence of flooding.
"""

def stations_level_over_threshold(stations, tol):
    """Return all stations with a RELATIVE level greater than a tolerance (tol).
    """
    return [
        (station, station.relative_water_level()) 
        for station in stations
        if station.relative_water_level() != None 
        and station.relative_water_level() > tol
        ]

def stations_highest_rel_level(stations, N):
    """Returns N most stations with the highest relative water levels.
    """

    #Trim stations with bad data
    stations = [station for station in stations if station.relative_water_level() != None]
    #Sort stations by attribute
    stations.sort(
        key=lambda station: station.relative_water_level(),
        reverse=True
        )

    #Splice
    return stations[:N]