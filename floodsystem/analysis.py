import numpy as np
import matplotlib

def polyfit(dates, levels, p):
    float_dates = matplotlib.dates.date2num(dates)

    p_coeff = np.polyfit(float_dates-float_dates[0], levels, p)

    poly = np.poly1d(p_coeff)
    return (poly, float_dates[0])