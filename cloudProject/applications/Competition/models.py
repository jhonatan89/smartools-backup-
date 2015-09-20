from django.db import models
from django.contrib.auth.models import User

from django.utils.encoding import smart_unicode


class Competition(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='ImageCompetitions/%Y/%m/%d')
    startDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    endDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    description = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    active = models.BooleanField()
    # company = models.ForeignKey(Company, null=True)
    company = models.ForeignKey(User)

    def __unicode__(self):
        title = "%s" % (smart_unicode(self.name))
        return title

    def get_competition_url(self):
        # return "http://" + platform.node() + ":8000" + "/competitions/%s/" % (self.id)
        return "http://127.0.0.1:8000" + "/competitions/%s/show/" % (self.id)

    def get_finish_competition_url(self):
        return "/competitions/%s/finish/" % (self.id)

    def get_edit_competition_url(self):
        return "/competitions/%s/edit/" % (self.id)

    def get_upload_video_url(self):
        return "competitions/%s/upload/" % (self.id)
