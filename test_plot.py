from socket import IPPORT_RESERVED
from floodsystem.plot import *
from datetime import datetime
from floodsystem.station import MonitoringStation


def test_plot_water_levels():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s.latest_level = 10

    assert plot_water_levels(s, "hello",[0.314]) == None
    assert plot_water_levels(s, [datetime(2022,1,15,12,13,14)], "hello") == None
    assert plot_water_levels(s, [], []) == None
    assert plot_water_levels(s, ["hello"], [0.344]) == None
    assert plot_water_levels(s, [datetime(2022,1,15,12,13,14)], ["hello"]) == None
    assert plot_water_levels("hello", [datetime(2022,1,15,12,13,14)], ["hello"]) == None


def test_plot_water_level_with_fit():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s.latest_level = 10

    assert plot_water_level_with_fit(s, "hello",[0.314], 3) == None
    assert plot_water_level_with_fit(s, [datetime(2022,1,15,12,13,14)], "hello", 3) == None
    assert plot_water_level_with_fit(s, [], [], 3) == None
    assert plot_water_level_with_fit(s, ["hello"], [0.344], 3) == None
    assert plot_water_level_with_fit(s, [datetime(2022,1,15,12,13,14)], ["hello"], 3) == None
    assert plot_water_level_with_fit("hello", [datetime(2022,1,15,12,13,14)], [0.314], 3) == None
    assert plot_water_level_with_fit(s, [datetime(2022,1,15,12,13,14)], [0.314], "hello") == None
    assert plot_water_level_with_fit(s, [datetime(2022,1,15,12,13,14)], [0.314], -2) == None
