import pandas as pd
import os
import h5py


def calculate_refractivity(df):
    Rd = 287.058  # in J/kg/K
    Rv = 461.52   # in J/kg/K
    epsilon = Rd / Rv
    
    obs_spechum = df['obs_specificHumidity']
    hofx_spechum = df['hofx_specificHumidity']
    p = df['pressure'] / 100  # hPA

    obs_mixr = obs_spechum / (1 - obs_spechum)
    hofx_mixr = hofx_spechum / (1 - hofx_spechum)

    df['obs_watervaporPressure'] = p * (obs_mixr / (obs_mixr + epsilon))
    df['hofx_watervaporPressure'] = p * (hofx_mixr / (hofx_mixr + epsilon))

    htemp = 'hofx_airTemperature'
    otemp = 'obs_airTemperature'
    pressure = 'pressure'
    hvapor = 'hofx_watervaporPressure'
    ovapor = 'obs_watervaporPressure'

    df['obs_refractivity'] = (77.6 * (df[pressure] / 100) / df[otemp]) + \
                             ((3.73 * 10**5) * df[ovapor] / (df[otemp] ** 2))

    df['hofx_refractivity'] = (77.6 * (df[pressure] / 100) / df[htemp]) + \
                               ((3.73 * 10**5) * df[hvapor] / (df[htemp] ** 2))

    return df
