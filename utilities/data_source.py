from utilities import read_utils

test_invalid_login_data=read_utils.get_csv_as_list("../test_data/test_invalid_login_data.csv")
print(test_invalid_login_data)

test_valid_request_demo=read_utils.get_sheet_as_list("../test_data/RequestDemoData.xlsx","Valid_Data")
print(test_valid_request_demo)

test_invalid_request_demo=read_utils.get_sheet_as_list("../test_data/RequestDemoData.xlsx","Invalid_Data")
print(test_invalid_request_demo)

test_invalid_account_creation=[("aaa","bbb","ccc@gmail.com","Test123","Test124","IND","Passwords do not match."),
                       ("aab","bbc","ccd@gmail.com","Test123","Test125","ALB","Passwords do not match.")
                       ]
print(test_invalid_account_creation)

test_password_criteria=[("aaa","bbb","aabbcc@gmail.com","Test123","Test123","IND","Your password must be at least 8 characters, must contain at least 1 letter, 1 number and 1 special character."),
                        ]
print(test_password_criteria)

