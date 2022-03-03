from distutils.command.build import build
from floodsystem.analysis import first_derivative, polyfit, second_derivative, data_complexity
from floodsystem.flood import *
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.geo import stations_by_river, towns_with_station
from floodsystem.stationdata import build_station_list, update_water_levels
import datetime
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from floodsystem.plot import plot_water_levels, plot_water_level_with_fit

def run():
    stations = build_station_list()
    update_water_levels(stations)

    for station in stations[:10]:
        if station.town is not None:
            risk = town_risk_assessment(stations, station.town)
            if risk in ["Severe", "High", "Moderate"]:
                print(station.town+": ", risk)

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()