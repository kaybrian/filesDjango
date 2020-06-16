from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Create your views here.
def index(request):
    return render(request,'youtube/index.html')

def uploads(request):
    if request.method == 'POST':
        uploadedFiles = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploadedFiles.name,uploadedFiles)
        url = fs.url(name)
    context = {'url':url}
    return render(request,'youtube/upload.html',context)