# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 14:31:51 2023

@author: PGS2KOR
"""
from continuous_range_finder import get_sorted_array

def get_number_of_readings_in_continuous_range(continuousrange, samples):
    sorted_samples = get_sorted_array(samples)
    number_of_readings = []
    for value in continuousrange:
        number_of_readings.append(sorted_samples.index(value[1]) - \
                                  sorted_samples.index(value[0]) + sorted_samples.count(value[1]))
    return number_of_readings