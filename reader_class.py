import json
import pickle
import csv
import sys
import os

current_directory = os.getcwd()
files_and_directories = os.listdir(current_directory)
files_only = [f for f in files_and_directories if os.path.isfile(os.path.join(current_directory, f))]
# csv_only = [f for f in files_and_directories if f.lower().endswith(".csv")]


class FileHandler:
    pkg_attr = None

    def read(self, file_name):
        with open(file_name, "rb") as f:
            return pkg_attr.load(f)

    def write(self, content, file_name):
        with open(file_name, "wb") as f:
            pkg_attr.dump(content, f)

class JsonHandler(FileHandler):
    pkg_attr = json

class PickleHandler(FileHandler):
    pkg_attr = pickle

class CsvHandler:
    def __init__(self):
        self.row_counter = 0

    def read_file(self, file_name):
        with open(file_name, newline="") as f:
            reader = csv.reader(f)
            data = []
            for row in reader:
                data.append(row)
                self.row_counter +=1
            return data
        
    def write_file(self, content, file_name):
        with open(file_name, 'w', newline="") as f:
            output = csv.writer(f)
            for row in content:
                output.writerow(row)