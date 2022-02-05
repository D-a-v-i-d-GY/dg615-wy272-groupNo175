# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    """Requirements for Task 1C"""

    # Build list of stations
    stations = build_station_list()

    # Set the reference point
    cambridge_coord = (52.2053, 0.1218)

    # Get the list of stations within 10 km radius from the reference point
    stations_within_rad = stations_within_radius(stations, cambridge_coord, 10)

    # Get the sorted list of the names of the stations
    stations_names_sorted = sorted([station.name for station in stations_within_rad])

    # Print the result
    print(stations_names_sorted)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
