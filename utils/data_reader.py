# import openpyxl library to read Excel files
import openpyxl


def get_login_data(file_path, sheet_name):
    """
    Read login data from Excel file
    """

    # load workbook
    workbook = openpyxl.load_workbook(file_path)

    # access sheet
    sheet = workbook[sheet_name]

    # create empty list to store data
    data = []

    # iterate through rows starting from row 2
    for row in sheet.iter_rows(min_row=2, values_only=True):

        # get username from column 1
        Username = row[0]

        # get password from column 2
        Password = row[1]

        # get Result from column 3
        Result = row[3]

        # append tuple to list
        data.append((Username, Password,Result))

    # return data list
    return data