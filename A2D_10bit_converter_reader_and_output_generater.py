# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 18:10:36 2023

@author: PGS2KOR
"""
from Limits import A2D_LIMITS
from continuous_range_and_number_of_readings_finder import\
    get_continuous_range_and_number_of_readings_and_generate_output

def convert_10bit_A2D_value_to_current_amps(value):
    current_value = round((value) / 34.067) - 15
    return current_value

def read_10bit_A2D_converter_and_generate_output(samples):
    current_samples = []
    continuous_range = []
    number_of_readings = []
    lowerlimit, upperlimit = A2D_LIMITS['10bit']
    for value in samples:
        if (value <= upperlimit):
            current_samples.append(abs(convert_10bit_A2D_value_to_current_amps(value)))
        else:
            print("An error in the values of A2D")
    continuous_range, number_of_readings = \
        get_continuous_range_and_number_of_readings_and_generate_output(current_samples)
    return (continuous_range, number_of_readings)


