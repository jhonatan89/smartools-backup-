from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'cloudProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('cloudProject.applications.Home.urls')),
    url(r'^account/', include('cloudProject.applications.Account.urls')),
    url(r'^competition/', include('cloudProject.applications.Competition.urls')),
]
