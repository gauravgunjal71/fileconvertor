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

        a4inpt = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
        layout_fun = img2pdf.get_layout_fun(a4inpt)
        with open(path_to_upload+"/sample.pdf", "wb") as f:
            f.write(img2pdf.convert(files_list, layout_fun=layout_fun))
        os.rename(path_to_upload+"/sample.pdf",path_to_upload+"/sample.txt")
        return render(request, 'jpgtopdf.html', {'url': str(res)})
    return render(request, 'jpgtopdf.html')