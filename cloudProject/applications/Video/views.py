from django.shortcuts import render, render_to_response

from cloudProject.applications.Video.forms import UploadVideo
from cloudProject.applications.Video.models import Video
from cloudProject.applications.Competition.models import Competition


# Create your views here.

def upload_video(request, id_competition):
    competition = Competition.objects.get(id=id_competition)
    if request.method == 'POST':
        form = UploadVideo(request.POST, request.FILES)
        if form.is_valid():
            new_video = Video(title=request.POST['title'], originalVideoPath=request.FILES['originalVideoPath'],
                              clientfirtsName=request.POST['clientfirtsName'],
                              clientLastName=request.POST['clientlastName'], description=request.POST['description'],
                              clientEmail=request.POST['clientEmail'], competition=competition)
            new_video.save(form)
            return render(request, 'Video/confirmation.html', {'competition': competition})
    else:
        form = UploadVideo()
        print competition.name
    return render(request, 'Video/index.html', {'form': form, 'competition': competition})


def confirmation_video(request):
    return render_to_response('Video/confirmation.html')


def get_video(request, id_competition):
    if request.method == 'GET':
        competition = Competition.objects.get(id=id_competition)
        list_video = Video.objects.filter(state='CON', competition=id_competition)
        return render(request, 'Competition/list_videos.html', {'videos': list_video, 'competition': competition})
    else:
        return render(request, 'Competition/list_videos.html')