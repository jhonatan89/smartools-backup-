__author__ = 'agilesfocused'
import boto
from boto.s3.key import Key
from cloudProject.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, MEDIAFILES_LOCATION


class S3Manager():

    def upload_media(self,file_type, file):
        try:
            print "method:upload_media"
            conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
            print "connected to S3"
            bucket = conn.get_bucket(AWS_STORAGE_BUCKET_NAME)
            print "connected to bucket"
            k = Key(bucket)
            print "Key(bucket)"
            k.key = 'media/' + file_type + file.name
            print "media file_type"
            #k.set_contents_from_filename(url_tmp + 'media/' + video_conv)
            print "ready to upload"
            k.set_contents_from_string(file.read())
            print "doit uploaded"
        except ValueError:
            print 'There is a error in the convert process'

