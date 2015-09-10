from django.conf.urls import url, patterns

urlpatterns = patterns('cloudProject.applications.Home.views',
      url(r'^$', 'index', name='init'),
)
