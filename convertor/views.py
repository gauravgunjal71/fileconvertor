from django.shortcuts import render, redirect
import img2pdf
import camelot
import pandas as pd
import string
import random
import os

# Create your views here.
def home(request):
    return render(request, 'index.html')

def fileuploads(request):
    if request.method == "POST":
        htmlpage = request.POST['htmlpage']
        files = request.FILES.getlist('files')
    return render(request, htmlpage, {'files':files})

def jpgToPdf(request):
    #img2pdf pip

    if request.method == "POST":
        # creating random folder name for each user
        res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
        path_to_upload = os.path.join('./convertor/static/uploaded_files/jpg2pdf', str(res))
        os.makedirs(path_to_upload)
        files = request.FILES
        files_list = []
        for file in files.getlist('files'):
            files_list.append(file)

        with open(path_to_upload+"/sample.pdf", "wb") as f:
            f.write(img2pdf.convert(files_list))
        return render(request, 'jpgtopdf.html', {'url': str(res)})
    return render(request, 'jpgtopdf.html')