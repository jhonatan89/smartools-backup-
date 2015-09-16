from django.conf.urls import url, patterns
from .views import finish,edit

urlpatterns = patterns('cloudProject.applications.Competition.views',
      url(r'^$', 'index', name='init'),
      url(r'^(?P<id_competition>\d+)/finish/$', finish.as_view(), name='finish'),
      url(r'^(?P<id_competition>\d+)/edit/$', edit.as_view(), name='edit'),
)
