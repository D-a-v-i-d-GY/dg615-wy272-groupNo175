from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():

    stations = build_station_list()
    update_water_levels(stations)
    TOL = 0.5
    
    over_tolerance_stations = stations_level_over_threshold(stations, TOL)
    for station, tol in over_tolerance_stations:
        print(
            over_tolerance_stations.index((station, tol))+1, station.name, tol
        )
    
    print("\n", len(over_tolerance_stations), "total stations surpassed the tolerance of", TOL,
    "out of", len(stations), "total stations.")


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
