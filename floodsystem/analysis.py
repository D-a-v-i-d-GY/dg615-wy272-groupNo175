import numpy as np
import matplotlib
from datetime import datetime
import math

def polyfit(dates, levels, p):
    """Fits a polynomial of p-th order to the data given (levels vs dates).
       levels is a list of floats, dates is a list of datetime.datetime, p is int"""

    # Check data consistency
    if not isinstance(dates, list):
        return None
    if not isinstance(levels, list):
        return None
    if len(dates) == 0 or len(levels) == 0:
        return None
    if not isinstance(dates[0], datetime):
        return None
    if not isinstance(levels[0], float):
        return None
    if not isinstance(p, int):
        return None
    if not p > 0:
        return None

    # Convert dates to floats
    float_dates = matplotlib.dates.date2num(dates)

    # Calculate the coefficients of the polynomial
    p_coeff = np.polyfit(float_dates-float_dates[0], levels, p)

    # Store result in poly1d class for convenient use
    poly = np.poly1d(p_coeff)
    return (poly, float_dates[0])


def first_derivative(poly, x):
    """Returns the first derivative of a polynomial function at 
       a given point, taking into account the date offset"""
    
    # Check data consistency
    if not isinstance(poly, tuple):
        return None
    if not isinstance(x, float):
        return None
    if len(poly) != 2:
        return None
    if not isinstance(poly[0], np.poly1d):
        return None
    if not isinstance(poly[1], float):
        return None

    x = x - poly[1]

    return sum([poly[0][i] * i * x ** (i - 1) for i in range(1, len(poly[0]) + 1)])


def second_derivative(poly, x):
    """Returns the first derivative of a polynomial function at 
       a given point, taking into account the date offset"""
    
    # Check data consistency
    if not isinstance(poly, tuple):
        return None
    if not isinstance(x, float):
        return None
    if len(poly) != 2:
        return None
    if not isinstance(poly[0], np.poly1d):
        return None
    if not isinstance(poly[1], float):
        return None

    x = x - poly[1]

    return sum([poly[0][i] * i * (i - 1) * x ** (i - 2) for i in range(2, len(poly[0]) + 1)])


def data_complexity(levels):
    """Assigns complexity to the given data"""

    levels = np.array(levels)
    return np.std(levels, axis=0)


def risk_level_allocation(station, first_der, second_der):
    """Assign flood risk level to the given station"""
    risk_levels = 0

    # Risk allocation criteria!
    relative_water_level = station.relative_water_level()
    if isinstance(relative_water_level, float) and relative_water_level >= 0:
        if relative_water_level <= 0.2:
            risk_levels += 4.0
        elif relative_water_level > 0.2 and relative_water_level <= 0.95:
            if second_der <= 0.0:
                risk_levels += 4.0
            elif first_der > 0 and math.log10(1.0 + first_der) > 2.0:
                risk_levels += 2.0
            else:
                risk_levels += 3.0
        elif relative_water_level > 0.95 and relative_water_level <= 2.0:
            if second_der <= 0.0:
                risk_levels += 3.0
            elif first_der > 0 and math.log10(1.0 + first_der) > 2.0:
                risk_levels += 1.0
            else:
                risk_levels += 2.0
        elif relative_water_level > 2.0 and relative_water_level <= 4.0:
            if second_der <= 0.0:
                risk_levels += 2.0
            else:
                risk_levels += 1.0
        else:
            risk_levels += 1.0
        # print(risk_levels, relative_water_level, first_der, second_der)

    return(risk_levels)