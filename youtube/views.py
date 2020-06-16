from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Create your views here.
def index(request):
    return render(request,'youtube/index.html')

def uploads(request):
    if request.method == 'POST':
        uploadedFiles = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploadedFiles.name,uploadedFiles)
    context = {}
    return render(request,'youtube/upload.html')