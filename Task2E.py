from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
import datetime

def run(): 
    
    stations = build_station_list()
    update_water_levels(stations)   
    N = 5
    DT = 10
    
    highest_stations = [
        station
        for station in stations_highest_rel_level(stations, N)
        ]

    for station in highest_stations:
        dates, levels = fetch_measure_levels(
            station.measure_id, 
            dt=datetime.timedelta(days=DT)
        )
        if not dates:
            continue

        plot_water_levels(station, dates, levels)
        

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()