import pandas as pd
import re

READ_EXCEPTION = """

    Run setput.py.
    If that does not work the file name is wrong or not in source folder.

"""
WRITE_EXCEPTION = """

    Run setup.py.

"""


# Removes all ', /, - \ from the table and replaces it with ~
def remove_invalid_characters(line):
    if(type(line) == str):
        return re.sub(r"'|/|-|\"", "~", line)
    else:
        return line

# Reads the table and formats it
def read_table(file_location):
    table = None
    try:
        # Read in the csv (input in data folder)
        print("Attempting to read file: {}".format(file_location))
        table = pd.read_csv(file_location, encoding='cp1252')
    except:
        raise Exception(READ_EXCEPTION)
    # Overwrite invalid characters
    return table.apply(remove_invalid_characters)

# Writes the table
def write_table(table, file_location):
    try:
        # Write the csv (output in output folder)
        table.to_csv(file_location, index=False)
        print("Cleaning was successful")
    except:
        raise Exception(WRITE_EXCEPTION)
