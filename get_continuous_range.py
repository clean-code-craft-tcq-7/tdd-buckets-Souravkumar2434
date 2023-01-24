# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 16:27:57 2023

@author: PGS2KOR
"""

def check_status_of_continuity_or_repeatidity_of_data(value):
    if(value <= 1):
        return True
    return False

def get_difference_between_the_consecutive_samples(samples , diff_of_samples):
    for i in range(len(samples) - 1):
        diff_of_samples.append(samples[i +1] - samples[i])
    diff_of_samples.insert(0 , 0)   #to make length equal to samples
    return diff_of_samples

def get_continuous_range_and_number_of_readings(samples):
    continuous_range = []
    continuous_range_indexes = []
    diff_of_samples = []
    number_of_readings = []

    diff_of_samples = get_difference_between_the_consecutive_samples(samples, diff_of_samples)
    for value in range(len(diff_of_samples)):
        if(check_status_of_continuity_or_repeatidity_of_data(diff_of_samples[value])):
            continuous_range_indexes.append(value)
        else:
            continuous_range.append([samples[continuous_range_indexes[0]], samples[continuous_range_indexes[-1]]])
            number_of_readings.append(len(continuous_range_indexes))
            continuous_range_indexes = []
            continuous_range_indexes.append(value)
    continuous_range.append([samples[continuous_range_indexes[0]], samples[continuous_range_indexes[-1]]])
    number_of_readings.append(len(continuous_range_indexes))
    return (continuous_range, number_of_readings)

