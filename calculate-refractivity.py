import pandas as pd
import os
import h5py


def calculate_refractivity(df):
    Rd = 287.058  # in J/kg/K
    Rv = 461.52   # in J/kg/K
    epsilon = Rd / Rv
    spechum = df['specificHumidity']
    p = df['pressure'] / 100  # hPA
    mixr = spechum / (1 - spechum)
    df['watervaporPressure'] = p * (mixr / (mixr + epsilon))
    df['refractivity'] = (77.6 * (df['pressure'] / 100) / df['airTemperature']) + \
                             ((3.73 * 10**5) * df['watervaporPressure'] / (df['airTemperature'] ** 2))
    return df
