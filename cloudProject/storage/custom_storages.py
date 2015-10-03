from django.conf import settings
from storages.backends.s3boto import S3BotoStorage


__author__ = 'jhonatan'

class MediaStorage(S3BotoStorage):
        location = settings.MEDIAFILES_LOCATION