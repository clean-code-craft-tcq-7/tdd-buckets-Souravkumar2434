from validate_input_data import check_input_data_is_ok

assert check_input_data_is_ok([]) == True
assert check_input_data_is_ok('') == False
