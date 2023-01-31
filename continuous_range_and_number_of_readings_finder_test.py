# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 12:47:12 2023

@author: PGS2KOR
"""
from validate_input_data import check_input_data_is_ok
from continuous_range_finder import get_continuous_range,\
    get_sorted_array, check_status_of_continuity_or_repeatidity_of_data,\
        get_difference_between_the_consecutive_samples,\
            calculate_continuous_range

# check validity of data
assert check_input_data_is_ok([]) == True
assert check_input_data_is_ok('') == False

#continuous range test
assert get_continuous_range([]) == []
assert get_continuous_range([1]) == []
assert get_continuous_range([4, 5]) == [[4, 5]]
assert get_continuous_range([4, 5, 6]) == [[4, 6]]
assert get_continuous_range([4, 6, 5, 7]) == [[4, 7]]
assert get_continuous_range([4, 5, 6, 9, 8, 10]) == [[4, 6], [8, 10]]

#Refactored continuous range test
assert get_sorted_array([]) == []
assert get_sorted_array([1]) == [1]
assert get_sorted_array([4, 5]) == [4, 5]
assert get_sorted_array([4, 6, 5, 7]) == [4, 5, 6, 7]

assert check_status_of_continuity_or_repeatidity_of_data(4) == False
assert check_status_of_continuity_or_repeatidity_of_data(1) == True

assert get_difference_between_the_consecutive_samples([4, 5], []) == [0, 1]
assert get_difference_between_the_consecutive_samples([4, 5, 6], []) == [0, 1, 1]
assert get_difference_between_the_consecutive_samples([4, 5, 6, 8, 9, 10], []) == [0, 1, 1, 2, 1, 1]

assert calculate_continuous_range([4, 5], []) == [[4, 5]]
assert calculate_continuous_range([4, 5, 6], []) == [[4, 6]]
assert calculate_continuous_range([4, 6, 5, 7], []) == [[4, 7]]
assert calculate_continuous_range([4, 5, 6, 9, 8, 10], []) == [[4, 6], [8, 10]]