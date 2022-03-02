from floodsystem.flood import *


def test_stations_level_over_threshold():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s.latest_level = 10

    assert stations_level_over_threshold(0, 0.5) == None
    assert stations_level_over_threshold([s], "hello") == None
    assert stations_level_over_threshold([], 0.5) == None
    assert stations_level_over_threshold(["hello"], 0.5) == None
    assert stations_level_over_threshold([s], -1) == None
    assert stations_level_over_threshold([s], 0.01) != None


def test_stations_highest_rel_level():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s.latest_level = 10

    assert stations_highest_rel_level(0, 5) == None
    assert stations_highest_rel_level([s], "hello") == None
    assert stations_highest_rel_level([], 5) == None
    assert stations_highest_rel_level(["hello"], 5) == None
    assert stations_highest_rel_level([s], -1) == None
    assert stations_highest_rel_level([s], 5) == None
    assert stations_highest_rel_level([s], 1) == [s]