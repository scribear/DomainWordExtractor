from PyPDF2 import PdfReader
import json
import os
import sys
import getopt
import jsonpickle
import string

import utils

### Made assuming that PDF has an Index. Stores data into a JSON file - if JSON already exists, adds only new words to the JSON.

# print(len(reader.pages)) # 19
if __name__ == "__main__":
    path = "./Class_Categories/"

    #Iterates over subdirectories in Class_Categories
    for class_type in os.listdir(path):
        subdirectory_path = os.path.join(path, class_type)
        page_str = ""
        myset = set()
        json_path = "words/" + class_type + ".json"

        #checks for file and that file is not empty. Populates myset with relevant data
        if os.path.exists(json_path) and os.path.getsize(json_path) > 0:
            json_data = utils.readJsonFile(json_path)
            myset = (jsonpickle.decode(json_data))

        for pdf in os.listdir(subdirectory_path):
            pdf_path = os.path.join(subdirectory_path, pdf)

            # read pdf
            reader = PdfReader(pdf_path)
            
            for page in reader.pages:
                page_str += page.extract_text()

        # page_str = str.lower(page_str) # all to lower case
        lines = page_str.split('\n')

        #Cleans list, stores phrases in myset
        word = ''
        for line in lines:
            for idx in range(len(line)):
                if str.isalpha(line[idx]) or line[idx] == " " or line[idx] == "'": # is normal
                    word += line[idx]
                else: # not a digit
                    if (word != 'Index' and word != 'Symbols' and len(word) > 2):
                        myset.add(word) # add the word/phrase
                    word = '' # reset the word

        # utils.writeJsonFile('test.json', page_str)
        utils.writeJsonFile(json_path, jsonpickle.encode(myset))
            