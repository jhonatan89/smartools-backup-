from django.conf.urls import url, patterns, include

from .views import finish, edit


urlpatterns = patterns('cloudProject.applications.Competition.views',
                       url(r'^$', 'index', name='init'),
                       url(r'^active_competitions/$', 'show_all_competitions', name='show_all_competitions'),
                       url(r'^(?P<id_competition>\d+)/finish/$', finish.as_view(), name='finish'),
                       url(r'^(?P<id_competition>)/edit/$', edit.as_view(), name='edit'),
                       url(r'^(?P<id_competition>\d+)/', include('cloudProject.applications.Video.urls')),
)
