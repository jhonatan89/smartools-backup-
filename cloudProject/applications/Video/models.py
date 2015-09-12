from django.db import models
from cloudProject.applications.Competition.models import Competition
from django.utils.encoding import smart_unicode

class Video(models.Model):
    VIDEO_STATES = (
        ('CON', 'Converted'),
        ('WFC', 'Waiting for conversion'),
    )
    clientfirtsName = models.CharField(max_length=200)
    clientLastName = models.CharField(max_length=200)
    clientEmail = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=255)
    uploadDate =models.DateTimeField(auto_now=False, auto_now_add=True)
    originalVideoPath = models.CharField(max_length=255)
    convertedVideoPath = models.CharField(max_length=255)
    state = models.CharField(max_length=3, choices=VIDEO_STATES, default='WFC')
    competition = models.ForeignKey(Competition, blank=True, null=True)
    video = models.FileField(upload_to='video/%Y/%m/%d', blank=True)

    def __unicode__(self):
        title = "%s %s %s" % (self.competition,smart_unicode(self.title), self.clientfirtsName, self.clientLastName)
        return title
