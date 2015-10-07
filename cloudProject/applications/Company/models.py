from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode

class Company(models.Model):
    name = models.CharField(max_length=200)
    nit = models.BigIntegerField()
    description = models.CharField(max_length=255)
    user = models.OneToOneField(User)

    def __unicode__(self):
        title = "%s" % (smart_unicode(self.name))
        return title

