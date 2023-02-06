# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 14:39:53 2023

@author: PGS2KOR
"""

def convert_12bit_A2D_value_to_current_amps(value):
    current_value = round((10 * value) / 4094)
    return current_value


def read_12bit_A2D_converter_and_generate_output(samples):
    return