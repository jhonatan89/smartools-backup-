from django.shortcuts import render, render_to_response
from cloudProject.applications.Video.forms import UploadVideo
from cloudProject.applications.MongoDB_APP.Competition import Competition
from cloudProject.applications.MongoDB_APP.Video import Video
from cloudProject.applications.MongoDB_APP.S3Manager import S3Manager
from cloudProject.applications.Account.Cookie_utils import get_cookie
from cloudProject.applications.Account.session import Session
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from datetime import datetime

def upload_video(request, id_competition):
    competition = Competition()
    competition.get(id_competition)
    if request.method == 'POST':
        form = UploadVideo(request.POST, request.FILES)
        if form.is_valid():
            file_path = S3Manager().upload_memory_media('media/Video/' + datetime.now().strftime("%Y/%m/%d"),
                                                        request.FILES['originalVideoPath'])
            Video().create(id_competition=id_competition,
                              title=request.POST['title'],
                              originalVideoPath=file_path,
                              clientfirtsName=request.POST['clientfirtsName'],
                              clientLastName=request.POST['clientlastName'],
                              description=request.POST['description'],
                              clientEmail=request.POST['clientEmail'])
            return render(request, 'Video/confirmation.html', {'competition': competition})
    else:
        form = UploadVideo()
    return render(request, 'Video/index.html', {'form': form, 'competition': competition})

def confirmation_video(request):
    return render_to_response('Video/confirmation.html')

def get_video(request, id_competition):
    list_video = []
    competition = Competition()
    competition.get(id_competition)
    company = get_cookie(request, 'userId')
    user = Session.verify_current_session(company)

    if user['isverify']:
        print "video logged"
        competition.get_videos(id_competition, "ANY")
        list_video = competition.videos
    else:
        print "video no logge"
        competition.get_videos(id_competition, "CON")
        list_video = competition.videos

    print "list_video"
    print list_video

    videos_per_page = 50
    paginator = Paginator(list_video, videos_per_page)
    page = request.GET.get('page')

    try:
        videos = paginator.page(page)
    except PageNotAnInteger:
        videos = paginator.page(1)
    except EmptyPage:
        videos = paginator.page(paginator.num_pages)

    if user['isverify']:
        return render(request, 'Competition/list_admin_videos.html',
                      {'videos': videos, 'competition': competition, 'user' : user})
    else:
        return render(request, 'Competition/list_public_videos.html',
                      {'videos': videos, 'competition': competition})