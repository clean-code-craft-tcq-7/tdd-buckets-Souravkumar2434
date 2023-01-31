# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 12:47:12 2023

@author: PGS2KOR
"""
from validate_input_data import check_input_data_is_ok

assert check_input_data_is_ok([]) == True
assert check_input_data_is_ok('') == False