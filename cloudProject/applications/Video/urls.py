from django.conf.urls import url, patterns

urlpatterns = patterns('cloudProject.applications.Video.views',
                       url(r'^upload/$', 'upload_video', name='upload_video'),
                       url(r'^show/$', 'get_video', name='get_video'),
)
