import os
import os.path


def get_all_subs_name(path):
    dir_names=[]
    file_names=[]
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_dir():
                dir_names.append(entry.name)
            if entry.is_file():
                file_names.append(entry.name)
    
    return {"dirs":dir_names,"files":file_names}

def get_project_abspath():
    return os.path.abspath(os.path.dirname(__name__))+'/'

def get_files_abspath():
    return get_project_abspath()+'note/static/files/'
