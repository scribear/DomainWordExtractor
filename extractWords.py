from PyPDF2 import PdfReader
import json
import os
import sys
import getopt
import jsonpickle

import utils

### Made assuming that PDF has an Index. Stores data into a JSON file - if JSON already exists, adds only new words to the JSON.

# print(len(reader.pages)) # 19
if __name__ == "__main__":
    #print(os.listdir('./pdf'))
    path = "./Class_Categories/"
    for class_type in os.listdir(path):
        subdirectory_path = os.path.join(path, class_type)
        for pdf in os.listdir(subdirectory_path):
            pdf_path = os.path.join(subdirectory_path, pdf)
            myset = set()
            json_path = "words/" + class_type + ".json"

            #checks for file and that file is not empty. Populates myset with relevant data
            if os.path.exists(json_path) and os.path.getsize(json_path) > 0:
                json_data = utils.readJsonFile(json_path)
                myset = (jsonpickle.decode(json_data))
                # raise SystemExit('File is not python set')
                # exit(-1)

            # read pdf
            reader = PdfReader(pdf_path)
            page_str = ""
            
            for page in reader.pages:
                page_str += page.extract_text()
                # print(page_str)

            # page_str = str.lower(page_str) # all to lower case
            lines = page_str.split('\n')

            #Cleans list, stores phrases in myset
            word = ''
            for line in lines:
                for idx in range(len(line)):
                    if str.isdigit(line[idx]): # is a digit
                        if (word != 'Index' and word != 'Symbols'):
                            myset.add(word) # add the word/phrase
                        word = '' # reset the word
                    else: # not a digit
                        word += line[idx]

            # utils.writeJsonFile('test.json', page_str)
            utils.writeJsonFile(json_path, jsonpickle.encode(myset))
            

        # #Fetch pdf path from CLI
        # print("Type the full file name of the PDF you are trying to read from (keep relevant PDFs in PDF folder):")
        # pdf_path = "./pdf/" + input() + ".pdf"

        # #Fetch json path from CLI
        # print("If there is already an existing JSON with relevant data input it here. \n Otherwise, write the name of the JSON file you would like to store the data in (keep relevant JSONs in words folder):")
        # json_path = "words/" + input() + ".json"

        # # read json set
        