from django.conf.urls import url, patterns

urlpatterns = patterns('cloudProject.applications.Video.views',
      url(r'^$','upload_video', name='upload_video'),
      url(r'^confirmation/$', 'confirmation_video', name='confirmation_video'),
)