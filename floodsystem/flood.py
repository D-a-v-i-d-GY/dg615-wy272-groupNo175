"""This module contains a collection of functions related to
predicting the occurence of flooding.
"""


from floodsystem.plot import plot_water_level_with_fit
from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_by_towns
from floodsystem.analysis import data_complexity, first_derivative, polyfit, second_derivative, risk_level_allocation
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import matplotlib
import matplotlib.pyplot as plt
import math
import numpy as np

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


def town_risk_assessment(stations, town, DT=0.5):
    """Returns a warning level for a given town"""

    # Get the towns dictionary
    town_dict = stations_by_towns(stations)

    # Get the target rivers
    target_stations = town_dict[town]

    risk_level = 0
    quantity = -1

    # Estimate the risk level for each station in the town
    for station in target_stations:
        dates, levels = fetch_measure_levels(
        station.measure_id, 
        dt=datetime.timedelta(days=DT)
    )
        if not dates:
            continue
        
        x = matplotlib.dates.date2num(datetime.datetime.now() + datetime.timedelta(days=0))

        if station.typical_range != None:
            low, high = station.typical_range
        
        # Get the relative data
        levels = [(levels[i]-low) / (high - low) for i in range(len(levels))]

        # Set polynomial order depending on the given data complexity
        p = min(math.ceil(95 * (data_complexity(levels) ** 0.95)), 20)
        p = max(p, 5)
        # print(p)

        # Get the fitting polynomial and its derivatives at the current time
        poly = polyfit(dates, levels, p)
        first_der  = first_derivative(poly, x)
        second_der = second_derivative(poly, x)

        # plot_water_level_with_fit(station, dates, levels, p)
        # plt.show()
        
        
        if quantity == -1:
            quantity = 0

        rla = risk_level_allocation(station, first_der, second_der)
        quantity += 1
        risk_level += rla
    
    # If no data available return None
    if quantity == -1:
        return None
    
    # Calculate the average risk level for the town
    total_risk_level = math.ceil(risk_level / quantity)
    warnings = ["", "severe", "high", "moderate", "low"]

    return warnings[total_risk_level] 

