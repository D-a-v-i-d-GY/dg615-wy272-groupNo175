from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river

def run():
    """Requirements for Task 1D"""

    # Part 1 of Task D
    # Build list of stations
    stations = build_station_list()

    # Get the list of rivers with stations
    rivers_with_stat = rivers_with_station(stations)

    # Print the quantity of rivers and names of first 10 rivers in alphabetical order
    print(len(rivers_with_stat), " stations. First 10 - ", sorted(rivers_with_stat)[:10], "\n")


    # Part 2 of Task D
    # Get the dictionary of rivers
    river_dict = stations_by_river(stations)
    
    # For each river of interest print the names of the stations in
    rivers_of_interest = ["River Aire", "River Cam", "River Thames"]
    for river in rivers_of_interest:
        print(f"{river}: ", sorted(river_dict[river]), "\n")

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()