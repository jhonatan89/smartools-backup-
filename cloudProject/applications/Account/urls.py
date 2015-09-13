from django.conf.urls import url, patterns
from .views import signin,signup
from django.views.generic import TemplateView

urlpatterns = patterns('cloudProject.applications.Account.views',
      url(r'^signout/$', 'signout', name='vsingout'),
      url(r'^signin/$',signin.as_view(),name='signin'),
      url(r'^signup/$',signup.as_view(),name='signup'),
)
