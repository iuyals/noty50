from django.shortcuts import render
from django.contrib.staticfiles.storage import staticfiles_storage

import os
import os.path

from . import helper

# Create your views here.

def index(request):
    path=helper.get_files_abspath()
    if request.method=='POST':
        uploaded_file=request.FILES['upfile']
        with open(path+uploaded_file.name,'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
        return render(request,'notice.html',context={"msg":'your file saved'})
    
    all_subs_names=helper.get_all_subs_info(path)
    context={"dirs":all_subs_names['dirs'],
        "files":all_subs_names['files']}
    return render(request,'file/index.html',context=context);

