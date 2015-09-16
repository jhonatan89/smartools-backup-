from subprocess import Popen

import kronos

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
        except:
            print 'There is a error for this process, verify or install ffmpeg'
    else:
        print 'There aren\'t videos for convert'
