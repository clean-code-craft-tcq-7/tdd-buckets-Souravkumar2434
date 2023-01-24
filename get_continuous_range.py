# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 16:27:57 2023

@author: PGS2KOR
"""

def check_status_of_continuity_or_repeatidity_of_data(value):
    if(value <= 1):
        return True
    return False

def get_difference_between_the_consecutive_samples(samples, diff_of_samples):
    for i in range(len(samples) - 1):
        diff_of_samples.append(samples[i +1] - samples[i])
    diff_of_samples.insert(0,0)   #to make length equal to samples
    return diff_of_samples


