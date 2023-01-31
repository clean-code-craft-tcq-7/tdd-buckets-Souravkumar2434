# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 12:47:12 2023

@author: PGS2KOR
"""
from validate_input_data import check_input_data_is_ok
from continuous_range_finder import get_continuous_range

# check validity of data
assert check_input_data_is_ok([]) == True
assert check_input_data_is_ok('') == False

#continuous range test
assert get_continuous_range([]) == []
assert get_continuous_range([1]) == []
assert get_continuous_range([4, 5]) == [[4 - 5]]
assert get_continuous_range([4, 5, 6]) == [[4 - 6]]
assert get_continuous_range([4, 6, 5, 7]) == [[4 - 7]]
assert get_continuous_range([4, 5, 6, 9, 8, 10]) == [[4 - 6], [8 - 10]]
