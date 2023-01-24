# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 16:12:57 2023

@author: PGS2KOR
"""

import numpy as np

assert check_validity_of_input_data([4,5]) == "<class 'list'>"
assert check_validity_of_input_data(np.array([4,5])) == "<class 'numpy.ndarray'>"
assert get_continuous_range([4,5]) == "Range, Readings\n4-5, 2"