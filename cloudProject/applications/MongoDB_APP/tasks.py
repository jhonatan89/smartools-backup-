from subprocess import Popen
import boto
from boto.s3.key import Key
from django.core.mail import send_mail
import os
from cloudProject.applications.MongoDB_APP.Video import Video
from cloudProject.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, MEDIAFILES_LOCATION

from cloudProject.celery import app


@app.task(bind=True)
def video_convert(self,id):
    print "Entro a la sqs"
    print str(id) + "title"
    url_tmp = '/app/media/video/'
    video = Video()
    video.get(id,"ANY")


    try:
        conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
        bucket = conn.get_bucket(AWS_STORAGE_BUCKET_NAME)
        video_file = bucket.get_key(str(video.originalVideoPath))
        # if not os.path.exists(os.path.dirname(video_file.name)):
        #     print "entro a crear"
        #     os.makedirs(os.path.dirname(video_file.name))
        print "ejemplo " + url_tmp + str(os.path.basename(video.originalVideoPath))
        video_file.get_contents_to_filename(url_tmp + str(os.path.basename(video.originalVideoPath)))
        video_conv = video.originalVideoPath + '.conv.mp4'
        Popen(['ffmpeg', '-i', video_file.name, video_conv]).wait()
        k = Key(bucket)
        k.key = video_conv
        k.set_contents_from_filename(video_conv)
        video.convertedVideoPath = video_conv
        video.update_to_uploaded()
        message = '<h2>Hi! ' + video.clientfirtsName + ' ' + video.clientLastName + ',</h2><br>' + '<h3>You already can watch your video in our website</h3>' + '<br>' + '<strong>Video:</strong> ' + video.title + '<br>' + '<strong>Video description:</strong> ' + video.description + '<br>' + 'Thanks' + '<br><br>' + 'Sm@rtTools 2015'
        send_mail('You already is in the competition ', '', 'smarttoolssaas@gmail.com', [video.clientEmail],fail_silently=False, html_message=message)
    except ValueError:
        print 'There is a error in the convert process'