
from cloudProject.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, MEDIAFILES_LOCATION
import boto

class CloudFrontManager():

    conn_S3 = ""
    conn_CF = ""

    def __init__(self):
        self.conn_S3 = boto.connect_s3(aws_access_key_id=AWS_ACCESS_KEY_ID,
                                                  aws_secret_access_key =AWS_SECRET_ACCESS_KEY)
        self.conn_CF = boto.connect_cloudfront(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)

    def get_distributions(self):
        return self.conn_CF.get_all_distributions()

    def get_first_distribution(self,rs):
        ds = rs[1]
        return ds.get_distribution()

    def build_cloudfront_video_url(self, file):
        ds = self.get_first_distribution(self.get_distributions())
        return "rtmp://" + ds.domain_name + file.name
