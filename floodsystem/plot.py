import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from .analysis import polyfit
from datetime import datetime
from floodsystem.station import MonitoringStation

def plot_water_levels(station, dates, levels):
    """Plots the level of water at a given station vs date"""
    # Check data consistency
    if not isinstance(dates, list):
        return None
    if not isinstance(levels, list):
        return None
    if len(dates) == 0 or len(levels) == 0:
        return None
    if not isinstance(dates[0], datetime):
        return None
    if not isinstance(levels[0], float):
        return None
    if not isinstance(station, MonitoringStation):
        return None

    plt.plot(dates, levels)

    plt.xlabel("Date")
    plt.ylabel("Water Level / m")
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.tight_layout()
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    """Plots the level of water at a given station along with the fitting function vs date"""
    # Check data consistency
    if not isinstance(dates, list):
        return None
    if not isinstance(levels, list):
        return None
    if len(dates) == 0 or len(levels) == 0:
        return None
    if not isinstance(dates[0], datetime):
        return None
    if not isinstance(levels[0], float):
        return None
    if not isinstance(station, MonitoringStation):
        return None
    if not isinstance(p, int):
        return None
    if p < 0:
        return None
    
    plt.plot(dates, levels)

    poly, d0 = polyfit(dates, levels, p)
    float_dates = matplotlib.dates.date2num(dates)
    x1 = np.linspace(float_dates[0], float_dates[-1], 30)
    plt.plot(x1, poly(x1-d0))  

    plt.xlabel("Date")
    plt.ylabel("Water Level / m")
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.hlines(station.typical_range, xmin=x1[0], xmax=x1[-1])

    plt.tight_layout()
    plt.show()