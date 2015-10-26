from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from cloudProject.applications.MongoDB_APP.connection_params import Connection
from cloudProject.applications.Video.forms import UploadVideo
from cloudProject.applications.MongoDB_APP.Competition import Competition
from cloudProject.applications.MongoDB_APP.S3Manager import S3Manager


# Create your views here.

def upload_video(request, id_competition):
    competition = Competition.objects.get(id=id_competition)
    if request.method == 'POST':
        form = UploadVideo(request.POST, request.FILES)
        if form.is_valid():
            file_path = S3Manager().upload_media('media/ImageCompetitions', request.FILES['originalVideoPath'])
            new_video = Video(title=request.POST['title'],
                              originalVideoPath=file_path,
                              clientfirtsName=request.POST['clientfirtsName'],
                              clientLastName=request.POST['clientlastName'],
                              description=request.POST['description'],
                              clientEmail=request.POST['clientEmail'],
                              competition=competition)
            new_video.save(form)
            return render(request, 'Video/confirmation.html', {'competition': competition})
    else:
        form = UploadVideo()
        print competition.name
    return render(request, 'Video/index.html', {'form': form, 'competition': competition})

def confirmation_video(request):
    return render_to_response('Video/confirmation.html')

def get_video(request, id_competition):
    print "methon:get_video"
    print "id_competition"
    print id_competition
    competition = Competition().get(id_competition)
    print competition
    videos_per_page = 50
    url = "/competitions/" + id_competition
    #print url + " url"
    #competition = Connection().db.Competition.find_one({ "url" : url})
    videos = []
    return render(request, 'Competition/list_public_videos.html',
                    {'videos': videos, 'competition': competition})