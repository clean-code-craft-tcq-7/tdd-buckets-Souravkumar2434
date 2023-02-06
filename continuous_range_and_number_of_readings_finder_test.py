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
from number_of_readings_in_continuous_range_finder\
    import get_number_of_readings_in_continuous_range
from continuous_range_and_number_of_readings_finder\
    import get_continuous_range_and_number_of_readings_and_generate_output
from output_in_csv_format import create_csv_format_string
from A2D_12bit_converter_reader_and_output_generater import\
    read_12bit_A2D_converter_and_generate_output,\
        convert_12bit_A2D_value_to_current_amps
from A2D_10bit_converter_reader_and_output_generater import\
    convert_10bit_A2D_value_to_current_amps,\
        read_10bit_A2D_converter_and_generate_output

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


#number of readings test
assert get_number_of_readings_in_continuous_range([], []) == []
assert get_number_of_readings_in_continuous_range([[4, 5]], [4, 5]) == [2]
assert get_number_of_readings_in_continuous_range([[4, 6]], [4, 5, 6]) == [3]
assert get_number_of_readings_in_continuous_range([[4, 7]], [4, 5, 6, 7]) == [4]
assert get_number_of_readings_in_continuous_range([[4, 6] , [8, 10]], [4, 5, 6, 8, 9, 10]) == [3, 3]

#creating output in csv format test
assert create_csv_format_string([[4, 5]], [2]) == "Range, Readings\n4-5, 2"
assert create_csv_format_string([[4, 5], [7, 8]], [2, 2]) == "Range, Readings\n4-5, 2\n7-8, 2"

#continuous_range_and_number_of_readings test
assert get_continuous_range_and_number_of_readings_and_generate_output([]) == ([],[])
assert get_continuous_range_and_number_of_readings_and_generate_output('') == ([],[])
assert get_continuous_range_and_number_of_readings_and_generate_output([1]) == ([],[])
assert get_continuous_range_and_number_of_readings_and_generate_output([4, 5]) == ([[4, 5]],[2])
assert get_continuous_range_and_number_of_readings_and_generate_output([4, 5, 6]) == ([[4, 6]],[3])
assert get_continuous_range_and_number_of_readings_and_generate_output([4, 6, 5, 7]) == ([[4, 7]],[4])
assert get_continuous_range_and_number_of_readings_and_generate_output([4, 5, 6, 9, 8, 10]) == ([[4, 6], [8, 10]],[3, 3])

#A2D_12bit_converter_reader_and_output_generater test

assert read_12bit_A2D_converter_and_generate_output([0, 400, 700, 1146]) == ([[0, 3]], [4])

#ignoring error readings tests
assert read_12bit_A2D_converter_and_generate_output([0, 400, 700, 1146, 2047, 2456, 4095]) == ([[0, 3], [5, 6]], [4, 2])
assert read_12bit_A2D_converter_and_generate_output([4095, 4096, 4097, 4098, 4099]) == ([], [])

#12bit_input_into_amps_converter test

assert convert_12bit_A2D_value_to_current_amps(0) == 0
assert convert_12bit_A2D_value_to_current_amps(400) == 1
assert convert_12bit_A2D_value_to_current_amps(4094) == 10

#A2D_10bit_converter_reader_and_output_generater test

assert read_10bit_A2D_converter_and_generate_output([0, 34, 68, 102]) == ([[12, 15]], [4])

#ignoring error readings tests
assert read_10bit_A2D_converter_and_generate_output([0, 34, 68, 102, 511, 545, 580]) == ([[0, 2], [12, 15]], [3, 4])
assert read_10bit_A2D_converter_and_generate_output([1024, 1025, 1026, 1027, 1028]) == ([], [])

#12bit_input_into_amps_converter test

assert convert_10bit_A2D_value_to_current_amps(0) == -15
assert convert_10bit_A2D_value_to_current_amps(1022) == 15
assert convert_10bit_A2D_value_to_current_amps(511) == 0
assert convert_10bit_A2D_value_to_current_amps(102) == -12
assert convert_10bit_A2D_value_to_current_amps(920) == 12


