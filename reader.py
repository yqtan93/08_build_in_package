# import required function
import csv
import sys
import os

current_directory = os.getcwd()
files_and_directories = os.listdir(current_directory)
files_only = [f for f in files_and_directories if os.path.isfile(os.path.join(current_directory))]

# set argv for in and out file
in_file = sys.argv[1]
out_file = sys.argv[2]

# read from source file
try:
    with open(in_file, newline="") as f:
        reader = csv.reader(f)
except FileNotFoundError:
    print(f"The file {in_file} doesn't exist in current directory.")
    print("Existing files in current directories: ")
    for f in files_only:
        print(f)
except IsADirectoryError:
    print(f"{in_file} is a directory. Please enter the name of a file.")
    print("Existing files in current directories: ")
    for f in files_only:
        print(f)

# lopp through the rest of argv

for i in (len(sys.argv) - 3):
    change = sys.argv[i]



# change csv based on user input


# write changes to source file