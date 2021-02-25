import os
import string
import shutil

def get_files_out():
    # 1 get file names from folder
    dir_list = [d for d in os.listdir(r"/Users/eduardorosas/Downloads/fonts") if os.path.isdir(os.path.join(r"/Users/eduardorosas/Downloads/fonts", d))] # r stands for raw
    os.chdir(r"/Users/eduardorosas/Downloads/fonts")
    # 2 rename files
    for directory in dir_list:
        onlyfiles = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        for file_name in onlyfiles:
            if not os.path.exists(os.path.join("/Users/eduardorosas/Downloads/fonts/" + directory, file_name)):
                shutil.move(os.path.join("/Users/eduardorosas/Downloads/fonts/" + directory, file_name), "/Users/eduardorosas/Downloads/fonts/all/")
            else:
                shutil.move(os.path.join("/Users/eduardorosas/Downloads/fonts/" + directory, file_name), "/Users/eduardorosas/Downloads/fonts/all/"+file_name+"_2")

get_files_out()
