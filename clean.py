from src.file import read_table, write_table
from src.lib import run_all_modifiers
import sys

PROGRAM_ARGUMENT_EXCEPTION = """
    
    When running clean.py, type the file name after.
    Example:
        python clean.py data.csv

"""


#Read in the file
num = len(sys.argv)
print(num)
if num<2:
    raise Exception(PROGRAM_ARGUMENT_EXCEPTION)

FILE = sys.argv[1]
PROFILES = sys.argv[2:]

INPUT_LOCATION = "source/{}".format(FILE)
OUTPUT_LOCATION = "output/{}".format(FILE)


# Read (also removes bad characters)
df = read_table(INPUT_LOCATION)

# Apply profiles
df = run_all_modifiers(FILE, df)

# Write
write_table(df, OUTPUT_LOCATION)