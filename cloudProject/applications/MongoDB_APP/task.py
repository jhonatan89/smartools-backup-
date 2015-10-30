from subprocess import Popen
import boto
from boto.s3.key import Key
from django.core.mail import send_mail
import os
from cloudProject.applications.Video.models import Video
from cloudProject.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, MEDIAFILES_LOCATION

from cloudProject.celery import app


@app.task(bind=True)
def video_convert(self,id):
    print "Entro a la sqs"
    print str(id) + "title"
    url_tmp = '/tmp/'
    video = Video.objects.get(id=id)

    try:
        conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
        bucket = conn.get_bucket(AWS_STORAGE_BUCKET_NAME)
        video_file = bucket.get_key('media/' + str(video.originalVideoPath))
        if not os.path.exists(url_tmp + 'media/video'):
            os.makedirs(url_tmp + 'media/video')
        video_file.get_contents_to_filename(url_tmp + video_file.name)
        video_conv = video.originalVideoPath.name + '.conv.mp4'
        Popen(['ffmpeg', '-i', url_tmp + video_file.name, url_tmp + 'media/' + video_conv]).wait()
        k = Key(bucket)
        k.key = 'media/' + video_conv
        k.set_contents_from_filename(url_tmp + 'media/' + video_conv)
        video.state = 'CON'
        video.convertedVideoPath = video_conv
        video.save()
        message = '<h2>Hola ' + video.clientfirtsName + ' ' + video.clientLastName + ',</h2><br>' + '<h3>You already can watch your video in our website</h3>' + '<br>' + '<strong>Video:</strong> ' + video.title + '<br>' + '<strong>Video description:</strong> ' + video.description + '<br>' + 'Thanks' + '<br><br>' + 'Sm@rtTools 2015'
        send_mail('You already is in the competition ', '', 'smarttoolssaas@gmail.com', [video.clientEmail],fail_silently=False, html_message=message)
    except ValueError:
        print 'There is a error in the convert process'