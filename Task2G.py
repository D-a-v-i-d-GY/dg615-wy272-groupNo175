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


stations = build_station_list()
update_water_levels(stations)   

for station in stations[:10]:
    dates, levels = fetch_measure_levels(station.measure_id, datetime.timedelta(days=1))
    print(town_risk_assessment(stations, station.town))