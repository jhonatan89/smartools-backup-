import kronos

from cloudProject.applications.Video.models import Video


__author__ = 'jhonatan'


@kronos.register('* * * * *')
def convert_videos():
    list_video = Video.objects.filter(state='WFC')
    print len(list_video)
    if len(list_video) > 0:
        try:
            for video_wfc in list_video:
                print video_wfc.title + ' .'

        except ValueError:
            print 'There is a error for this process'

    else:
        print 'There are Not videos for converted'