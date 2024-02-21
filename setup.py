import os

# Creates the source and output folder
paths = ["./source", "./output"]
for path in paths:
    if not os.path.isdir(path):
        os.makedirs(path)

# Message on how to use
print("""
    Place the source files into the source folder.
    After the source files are in the folder, run with:
        python clean.py <file_name>
""")