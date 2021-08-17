import os
import shutil
import time

def remove_files(path):
    if not os.remove(path):
        print(f'{path}is removed sucsessfully')
    else:
        print('unable to remove')

def remove_folder(path):
    if not shutil.rmtree(path):
        print(f'{path}is removed sucsessfully')
    else:
        print('unable to remove')

def get_file_age(path):
    folder_time=os.stat(path).st_ctime
    return(folder_time)
    
