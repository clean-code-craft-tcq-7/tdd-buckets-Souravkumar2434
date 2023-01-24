# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 16:27:57 2023

@author: PGS2KOR
"""

def check_status_of_continuity_or_repeatidity_of_data(firstvalue, secondvalue):
    if(secondvalue- firstvalue == 1)\
        or (secondvalue- firstvalue == 0):
            return True
    return False

def get_continuous_range(samples):
    start_value = samples[0]
    next_value = sample[0]
    
    for sample in samples:
        if(check_status_of_continuity_or_repeatidity_of_data):
            next_value = sample
            continue
    return