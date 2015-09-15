from django.conf.urls import url, patterns
from .views import finish

urlpatterns = patterns('cloudProject.applications.Competition.views',
      url(r'^$', 'index', name='init'),
      url(r'^(?P<id_competition>\d+)/finish/$', finish.as_view(), name='finish'),
)
