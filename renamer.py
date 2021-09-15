from docx import Document
import re
import os

PATH = 'split'

#create dir for rename file
dir_name = 'Rename'
if not os.path.isdir(dir_name):
    os.mkdir(dir_name)

def find_id(document):
    for para in document.paragraphs:
        id = re.findall(r'کد ملی\W*:\W*(\d*)', para.text)
        if len(id) != 0:
            return id[0]

def get_list_file():
    return [dir for dir in os.listdir(PATH)]

for file in get_list_file():
    document = Document(PATH + "/" + file)
    id = find_id(document)
    document.save(dir_name + "/" + id + ".docx")
    
