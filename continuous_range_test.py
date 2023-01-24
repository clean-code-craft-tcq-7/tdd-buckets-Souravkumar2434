# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 16:12:57 2023

@author: PGS2KOR
"""
from check_validity_of_input_data import check_validity_of_input_data
from get_continuous_range import get_continuous_range,\
    check_status_of_continuity_or_repeatidity_of_data,\
        get_difference_between_the_consecutive_samples
 

assert check_validity_of_input_data([4,5]) == "<class 'list'>"
assert get_difference_between_the_consecutive_samples([4,5]) == [0,1]
assert check_status_of_continuity_or_repeatidity_of_data([4,5]) == True
assert get_continuous_range([4,5]) == "Range, Readings\n4-5, 2"

