import os
import os.path

def fsize_str(size):
    if size<1024:
        return str(size)+'bytes'
    if size<1024*1024:
        return str(round(size/1024,3))+'KB'
    else:
        return str(round(size/1024/1024,3))+'MB'

def get_all_subs_info(path):
    dir_infos=[]
    file_infos=[]
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_dir():
                dir_infos.append({'name':entry.name})
            if entry.is_file():
                file_infos.append({'name':entry.name,'size':fsize_str(entry.stat().st_size)})
    
    dir_infos.sort(key=lambda d: d['name'])
    file_infos.sort(key=lambda f: f['name'])
    return {"dirs":dir_infos,"files":file_infos}

def get_project_abspath():
    return os.path.abspath(os.path.dirname(__name__))+'/'

def get_files_abspath():
    return get_project_abspath()+'note/static/files/'
