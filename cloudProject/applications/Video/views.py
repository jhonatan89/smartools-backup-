from django.shortcuts import render, redirect, render_to_response

from cloudProject.applications.Video.forms import UploadVideo
from cloudProject.applications.Video.models import Video


# Create your views here.

def upload_video(request):
    if request.method == 'POST':
        form = UploadVideo(request.POST, request.FILES)
        if form.is_valid():
            new_video = Video(title=request.POST['title'], originalVideoPath=request.FILES['originalVideoPath'], clientfirtsName=request.POST['clientfirtsName'],
                              clientLastName=request.POST['clientlastName'], description=request.POST['description'],
                              clientEmail=request.POST['clientEmail'])
            new_video.save(form)
            return redirect('confirmation_video')
    else:
        form = UploadVideo()
    return render(request, 'Video/index.html', {'form': form})


def confirmation_video(request):
    return render_to_response('Video/confirmation.html')