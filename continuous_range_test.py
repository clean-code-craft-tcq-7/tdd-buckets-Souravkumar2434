# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 16:12:57 2023

@author: PGS2KOR
"""
from check_validity_of_input_data import check_input_data_is_valid
from get_continuous_range import get_continuous_range_and_number_of_readings,\
    check_status_of_continuity_or_repeatidity_of_data,\
        get_difference_between_the_consecutive_samples, get_sorted_array,\
            create_continuous_range_and_number_of_readings
from create_output_in_csv_format import create_csv_format_string


assert check_input_data_is_valid([4, 5]) == True
assert check_input_data_is_valid([4]) == False
assert get_sorted_array([5,4,6]) == [4,5,6]
assert get_difference_between_the_consecutive_samples([4, 5], []) == [0, 1]
assert check_status_of_continuity_or_repeatidity_of_data(4) == False
assert check_status_of_continuity_or_repeatidity_of_data(1) == True
assert create_continuous_range_and_number_of_readings([],[],[4,5]) == ([[4, 5]], [2])
assert get_continuous_range_and_number_of_readings([4, 5]) == ([[4, 5]], [2])
assert get_continuous_range_and_number_of_readings([4]) == ([], [])
assert get_continuous_range_and_number_of_readings([4, 5, 7, 8, 9]) == ([[4, 5], [7, 9]], [2, 3])
assert get_continuous_range_and_number_of_readings([5, 4, 8, 7, 9]) == ([[4, 5], [7, 9]], [2, 3])
assert create_csv_format_string([[4, 5], [7, 9]], [2, 3]) == 'Range, Readings\n4, 5, 2\n7, 9, 3'
