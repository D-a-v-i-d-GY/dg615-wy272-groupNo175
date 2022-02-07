# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        """Check that stations have consistent data:
            1) data is available
            2) reported high range > low range
        """
        # Check that data exists
        if not self.typical_range:
            return False

        # Check that data is tuple of len 2
        if type(self.typical_range) is tuple:
            if len(self.typical_range) != 2:
                return False
        else:
            return False

        # Check that max > min
        low, high = self.typical_range
        if low > high:
            return False
        
        # Data is consistent, return True
        return True

def inconsistent_typical_range_stations(stations):
    """Returns list of stations with inconsistent data"""

    # List of stations IF data is inconsistent
    i_stations = [station for station in stations if not station.typical_range_consistent()]

    return i_stations