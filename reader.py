# import required function
import csv
import sys
import os
from reader_class import FileHandler, JsonHandler, PickleHandler, CsvHandler

class FileNotSupportedError:
    pass

def get_handler(file_name):
    if file_name.endswith(".csv"):
        return CsvHandler()
    elif file_name.endswith(".pkl"):
        return PickleHandler()
    elif file_name.endswith(".json"):
        print("This is a JSON file.")
        return JsonHandler()
    else:
        raise FileNotSupportedError(f"File type {file_name} is not supported.")

if __name__ == "__main__":
    # set argv for in and out file
    in_file = sys.argv[1]
    out_file = sys.argv[2]

    # check input file validity
    if not os.path.exists(in_file):
        file_directory = os.path.split(in_file)[0]
        if not file_directory:
            file_directory = os.getcwd()
        other_files_in_directory = [
            f for f in os.listdir(file_directory) if f.lower().endswith(".csv") or f.lower().endswith(".pkl") or f.lower().endswith(".json")
            ]
    
    file = get_handler(in_file)
    data = file.read_file(in_file)
    print(data)
    row_counter = file.row_counter

    # loop through the rest of argv
    for i in sys.argv[3:]:
        change = i.split(',')
        
    # validate if change is in correct format
        if len(change) == 3:
            X, Y, value = change
            if int(X) > row_counter:
                print(f"\nRow number for {change} out of range. Skipping change...") 
            elif int(Y) > len(data[int(Y)]):
                print(f"\nColumn number for {change} out of range. Skipping change...")
            else:
                data[int(X)][int(Y)] = value
        else:
            print(f"\nChange {change} out of range. Skipping change...")

    file.write_file(data, out_file)

# Test commands
# CSV: reader.py in.csv out.csv 0,0,test 3,2,check



