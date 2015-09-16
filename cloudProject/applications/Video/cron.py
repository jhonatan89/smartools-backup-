from subprocess import Popen

import kronos

from cloudProject.applications.Video.models import Video
from cloudProject.settings import MEDIA_ROOT


__author__ = 'jhonatan'


@kronos.register('* * * * *')
def convert_videos():
    list_video = Video.objects.filter(state='WFC')
    print len(list_video)
    if len(list_video) > 0:
        try:
            for video_wfc in list_video:
                video_con = video_wfc.originalVideoPath.name + '.conv.mp4'
                Popen(['ffmpeg', '-i', video_wfc.originalVideoPath.name, video_con], cwd=MEDIA_ROOT).wait()
                video_wfc.state = 'CON'
                video_wfc.save()
        except:
            print 'There is a error for this process'

    else:
        print 'There are Not videos for converted'