# import required function
import csv
import sys
import os

current_directory = os.getcwd()
files_and_directories = os.listdir(current_directory)
# files_only = [f for f in files_and_directories if os.path.isfile(os.path.join(current_directory, f))]
csv_only = [f for f in files_and_directories if f.lower().endswith(".csv")]

# set argv for in and out file
in_file = sys.argv[1]
out_file = sys.argv[2]

# read from source file
try:
    with open(in_file, newline="") as f:
        reader = csv.reader(f)
        data = []
        for row in reader:
            data.append(row)
        print(data)

# display list of files in current directory if file is not found or input is not a file name
except FileNotFoundError:
    print(f"The file {in_file} doesn't exist in current directory.")
    print("Existing CSV files in current directories: ")
    for f in csv_only:
        print(f)
except IsADirectoryError:
    print(f"{in_file} is a directory. Please enter the name of a file.")
    print("Existing CSV files in current directories: ")
    for f in csv_only:
        print(f)
# file type validation
except csv.Error:
    print("File is not a .csv file. Please enter a .csv file.")
    print("Existing CSV files in current directories: ")
    for f in csv_only:
        print(f)

# loop through the rest of argv

for i in range(3, len(sys.argv)):
    change = sys.argv[i].split(',')
    X, Y, value = change
    data[int(X)][int(Y)] = value
# apply changes according to the user input
#     for X, Y, value in change:
#         data[X][Y] = value

print(data)

# write changes to output file
with open(out_file, 'w', newline="") as f:
    output = csv.writer(f)
    for row in data:
        output.writerow(row)
