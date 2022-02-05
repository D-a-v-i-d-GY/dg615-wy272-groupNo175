# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance


def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()

    # Set the reference point
    cambridge_coord = (52.2053, 0.1218)

    # Get the sorted by distance list
    stations_sorted = stations_by_distance(stations, cambridge_coord)

    # Print 10 closest and 10 furthest stations in format (station name, town, distance)
    closest_stations = stations_sorted[:10]
    furthest_stations = stations_sorted[-10:]

    closest_stations = [(station_dist[0].name, station_dist[0].town,
                         station_dist[1]) for station_dist in closest_stations]

    furthest_stations = [(station_dist[0].name, station_dist[0].town,
                         station_dist[1]) for station_dist in furthest_stations]

    print("Closest stations: ", closest_stations, "\n", "\n", "Furthest stations: ", furthest_stations)
    
if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
