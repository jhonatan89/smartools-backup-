from django.db import models
from cloudProject.applications.Company.models import Company

from django.utils.encoding import smart_unicode

class Competition(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=255)
    startDate =models.DateTimeField(auto_now=False, auto_now_add=True)
    endDate =models.DateTimeField(auto_now=False, auto_now_add=True)
    description = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    company = models.ForeignKey(Company)

    def __unicode__(self):
        title = "%s" % (smart_unicode(self.name))
        return title
