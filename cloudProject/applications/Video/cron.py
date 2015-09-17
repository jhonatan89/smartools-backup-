from subprocess import Popen

import kronos
from django.core.mail import send_mail

from cloudProject.applications.Video.models import Video
from cloudProject.settings import MEDIA_ROOT

__author__ = 'jhonatan'


@kronos.register('* * * * *')
def convert_videos():
    list_video = Video.objects.filter(state='WFC')
    if len(list_video) > 0:
        try:
            for video in list_video:
                video_conv = video.originalVideoPath.name + '.conv.mp4'
                Popen(['ffmpeg', '-i', MEDIA_ROOT + '/' + video.originalVideoPath.name,
                       MEDIA_ROOT + '/' + video_conv]).wait()
                video.state = 'CON'
                video.convertedVideoPath = video_conv
                video.save()
                message = '<h2>Hola ' + video.clientfirtsName + ' ' + video.clientLastName + ',</h2><br>' + '<h3>You already can see your video in our website</h3>' + '<br>' + '<strong>Video:</strong> ' + video.title + '<br>' + '<strong>Video description:</strong> ' + video.description + '<br>' + 'Thanks' + '<br><br>' + 'Sm@rtTools 2015'
                send_mail('You already is in the competition ', '', 'smarttoolssaas@example.com', [video.clientEmail],
                          fail_silently=False, html_message=message)
        except:
            print 'There is a error in the convert process'
    else:
        print 'There aren\'t videos for convert'
