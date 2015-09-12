from django.conf.urls import url, patterns
from .views import singin
from django.views.generic import TemplateView

urlpatterns = patterns('cloudProject.applications.Account.views',
      url(r'^singout/$', 'singout', name='vsingout'),
      url(r'^singin/$',singin.as_view(),name='singin'),
)
