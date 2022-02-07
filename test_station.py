# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

# Task 1F
def test_typical_range_consistent():

    # Default station characteristics
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    river = "River X"
    town = "My Town"

    # Create a station with NO DATA
    trange = None
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    assert not s.typical_range_consistent()

    # INVALID DATA
    trange = "apple"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    assert not s.typical_range_consistent()

    trange = [1, 2]
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    assert not s.typical_range_consistent()

    trange = (1)
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    assert not s.typical_range_consistent()

    # INCONSISTENT DATA
    trange = (5, 1)
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    assert not s.typical_range_consistent()

    # VALID DATA
    trange = (1, 10)
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    assert s.typical_range_consistent()

# Task 1F
def test_inconsistent_typical_range_stations():
    stations = build_station_list()
    
    i_stations = inconsistent_typical_range_stations(stations)

    # Check that the number of inconsistent stations does not exceed total
    assert len(i_stations) < len(stations)

    # Check that each station is inconsistent
    assert all([station.typical_range_consistent() for station in i_stations])

