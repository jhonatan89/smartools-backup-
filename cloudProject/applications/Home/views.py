from django.shortcuts import render_to_response, RequestContext

# Create your views here
from cloudProject.applications.Account.Cookie_utils import get_cookie
from cloudProject.applications.Account.session import Session


def index(request):
    user = Session.verify_current_session(get_cookie(request, 'userId'))
    return render_to_response('Home/index.html', {'user': user}, context_instance=RequestContext(request))


def forbidden(request):
    return render_to_response('Home/index.html', context_instance=RequestContext(request))


def about_us(request):
    user = Session.verify_current_session(get_cookie(request, 'userId'))
    return render_to_response('Home/about_us.html', {'user': user}, context_instance=RequestContext(request))