from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    """Requirements for Task 1C"""

    # Build list of stations
    stations = build_station_list()
    
    # Find first N stations
    N = 9
    n_rivers = rivers_by_station_number(stations, N)

    # Print the result
    print("Top", N, "rivers by monitoring stations:\n", n_rivers)

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***\n")
    run()