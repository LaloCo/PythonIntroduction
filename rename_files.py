import os
import string

def rename_files():
    # 1 get file names from folder
    file_list = os.listdir(r"C:\Users\lalor\Downloads\prank\prank") # r stands for raw
    os.chdir(r"C:\Users\lalor\Downloads\prank\prank")
    print(file_list)
    # 2 rename files
    for file_name in file_list:
        # Python 2 os.rename(file_name, file_name.translate(None, "0123456789"))
        # Python 3
        translation = str.maketrans(string.ascii_letters, string.ascii_letters, string.digits)
        os.rename(file_name, file_name.translate(translation))

rename_files()