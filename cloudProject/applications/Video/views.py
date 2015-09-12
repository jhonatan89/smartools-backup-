from django.shortcuts import render, redirect
from cloudProject.applications.Video.forms import UploadVideo
from cloudProject.applications.Video.models import Video

# Create your views here.

def upload_video(request):
    if request.method == 'POST':
        form = UploadVideo(request.POST, request.FILES)
        if form.is_valid():
            new_video = Video(title=request.POST['title'], video=request.FILES['video'], clientfirtsName=request.POST['clientfirtsName'],
                              clientLastName=request.POST['clientlastName'], description=request.POST['description'],
                              clientEmail=request.POST['clientEmail'])
            new_video.save(form)
            return redirect("upload_video")
    else:
        form = UploadVideo()
    return render(request, 'Video/index.html', {'form': form})