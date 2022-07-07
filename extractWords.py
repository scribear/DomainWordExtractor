from PyPDF2 import PdfReader
import os
import sys
import getopt
import jsonpickle

import utils

### Made assuming that PDF has an Index. Stores data into a JSON file.

# print(len(reader.pages)) # 19
if __name__ == "__main__":
    print(os.listdir('./pdf'))

    myset = set()
    reader = PdfReader("./pdf/biology-index.pdf")
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
    utils.writeJsonFile('words/bio_words.json', jsonpickle.encode(myset))