from django.shortcuts import render_to_response, RequestContext

# Create your views here
from cloudProject.applications.Account.Cookie_utils import get_cookie
from cloudProject.applications.Account.session import Session


def index(request):
    user_name = get_cookie(request,'userId')
    user_is_verify = Session().verify_current_session(get_cookie(request,'userId'))
    return render_to_response('Home/index.html', {"user": {"isverify": user_is_verify,"name": user_name }}, context=RequestContext(request))

def forbidden(request):
    return render_to_response('Home/index.html', context=RequestContext(request))

def about_us(request):
    return render_to_response('Home/about_us.html', context=RequestContext(request))