from django.shortcuts import render
from django.contrib.staticfiles.storage import staticfiles_storage

import os
import os.path ,requests

from . import helper 
# Create your views here.

def index(request):
    path=helper.get_files_abspath()
    if request.method=='POST':
        if 'upfile' in request.FILES.keys():
            uploaded_file=request.FILES['upfile']
            if len(request.POST['fname'])>0:
                fname=path+request.POST['fname']
            else:
                fname=path+uploaded_file.name
            with open(fname,'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
        elif len(request.POST['url'])>3 and len(request.POST['fname'])>0:
            helper.dlfile(request.POST['url'],fname=request.POST['fname'])
        else:
            return render(request,'notice.html',context={"msg":"invalid file or url"})

        return render(request,'notice.html',context={"msg":'your file saved'})
    
    all_subs_names=helper.get_all_subs_info(path)
    context={"dirs":all_subs_names['dirs'],
        "files":all_subs_names['files']}
    return render(request,'file/index.html',context=context);

