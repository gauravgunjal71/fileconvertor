from django.shortcuts import render, redirect
import camelot
import pandas as pd

# Create your views here.
def home(request):
    return render(request, 'index.html')

def fileuploads(request):
    if request.method == "POST":
        htmlpage = request.POST['htmlpage']
        files = request.FILES.getlist('files')
    return render(request, htmlpage, {'files':files})

def jpgToPdf(request):
    return render(request, 'jpgtopdf.html')