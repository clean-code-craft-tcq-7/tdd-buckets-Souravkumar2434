# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 17:21:36 2023

@author: PGS2KOR
"""

def create_csv_format_string(continuous_range, number_of_readings):
    csv_string = "Range, Readings"
    for value in range(len(continuous_range)):
        csv_string += "\n{}, {}".format(str(continuous_range[value])[1:-1], number_of_readings[value])
    return csv_string