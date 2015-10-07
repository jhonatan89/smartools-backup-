from subprocess import Popen
import boto
from boto.s3.key import Key
import kronos
from django.core.mail import send_mail
import os
from cloudProject.applications.Video.models import Video
from cloudProject.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, MEDIAFILES_LOCATION

__author__ = 'jhonatan'


@kronos.register('*/5 * * * *')
def convert_videos():
    url_tmp = '/tmp/'
    list_video = Video.objects.filter(state='WFC')
    if len(list_video) > 0:
        try:
            conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
            bucket = conn.get_bucket(AWS_STORAGE_BUCKET_NAME)
            for video in list_video:
                video.state = 'CIP'
                video.save()
                video_file = bucket.get_key('media/' + str(video.originalVideoPath))
                if not os.path.exists(url_tmp):
                    os.makedirs(url_tmp)
                video_file.get_contents_to_filename(url_tmp + video_file.name)
                video_conv = video_file.name + '.conv.mp4'
                Popen(['ffmpeg', '-i', url_tmp + video_file.name,
                       url_tmp + video_conv]).wait()
                k = Key(bucket)
                k.key = video_conv
                k.set_contents_from_filename(url_tmp + video_conv)
                video.state = 'CON'
                video.convertedVideoPath = video_conv
                video.save()
                message = '<h2>Hola ' + video.clientfirtsName + ' ' + video.clientLastName + ',</h2><br>' + '<h3>You already can watch your video in our website</h3>' + '<br>' + '<strong>Video:</strong> ' + video.title + '<br>' + '<strong>Video description:</strong> ' + video.description + '<br>' + 'Thanks' + '<br><br>' + 'Sm@rtTools 2015'
                send_mail('You already is in the competition ', '', 'smarttoolssaas@example.com', [video.clientEmail],
                          fail_silently=False, html_message=message)
        except ValueError:
            print 'There is a error in the convert process'
    else:
        print 'There aren\'t videos for convert'
