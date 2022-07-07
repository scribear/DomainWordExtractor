import json
import os

def cdRootDir():
    cur_dir = os.getcwd()
    while cur_dir != '/':
        os.chdir('../')
        cur_dir = os.getcwd()

# file_path = file_name; ends with json
def writeJsonFile(file_path, json_string):
    # write to a json file
    # Directly from dictionary
    with open(file_path, 'w') as outfile:
        json.dump(json_string, outfile)

# read; returns a dict
def readJsonFile(file_path):
    # read form a json file
    with open(file_path) as json_file:
        data = json.load(json_file)
        return data