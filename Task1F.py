from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    """Requirements for Task 1C"""

    # Build list of stations
    stations = build_station_list()
    
    # Find inconsistent stations
    i_stations = inconsistent_typical_range_stations(stations)

    # Print sorted names
    print(sorted([station.name for station in i_stations]))

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()