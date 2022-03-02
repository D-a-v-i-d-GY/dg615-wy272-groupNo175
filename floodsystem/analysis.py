import numpy as np
import matplotlib
from datetime import datetime

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


def derivative(poly, x):
    """Returns derivative of a polynomial function at 
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