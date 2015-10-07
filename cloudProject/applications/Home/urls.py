from django.conf.urls import url, patterns

urlpatterns = patterns('cloudProject.applications.Home.views',
      url(r'^$', 'index', name='init'),
      url(r'^about_us$', 'about_us', name='about_us'),
      url(r'^forbidden$', 'forbidden', name='forbidden'),
)
