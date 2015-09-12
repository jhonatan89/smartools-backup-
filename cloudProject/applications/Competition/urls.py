from django.conf.urls import url, patterns

urlpatterns = patterns('cloudProject.applications.Competition.views',
      url(r'^$', 'index', name='init'),
)
