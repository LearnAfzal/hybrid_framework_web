from utilities import read_utils

test_invalid_login_data=read_utils.get_csv_as_list("../test_data/test_invalid_login_data.csv")
print(test_invalid_login_data)

test_valid_request_demo=read_utils.get_sheet_as_list("../test_data/RequestDemoData.xlsx","Valid_Data")
print(test_valid_request_demo)

