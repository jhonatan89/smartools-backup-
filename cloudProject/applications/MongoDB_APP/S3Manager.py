__author__ = 'agilesfocused'
import boto
from boto.s3.key import Key
from cloudProject.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, MEDIAFILES_LOCATION


class S3Manager():

    def upload_media(self,file_type, file):
        try:
            conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
            bucket = conn.get_bucket(AWS_STORAGE_BUCKET_NAME)
            k = Key(bucket)
            k.key = 'media/' + file_type
            #k.set_contents_from_filename(url_tmp + 'media/' + video_conv)
            k.set_contents_from_string(file.read())
        except ValueError:
            print 'There is a error in the convert process'

