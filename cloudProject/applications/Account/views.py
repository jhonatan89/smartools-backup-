import json

from django.shortcuts import  HttpResponseRedirect,HttpResponse,render_to_response
from django.contrib import auth
from cloudProject.applications.Account.Cookie_utils import set_cookie
from session import Session
from django.contrib.auth.models import User, Group
from django.views.generic import TemplateView
from cloudProject.applications.MongoDB_APP.Company import Company


def signout(request):

    auth.logout(request)

    return HttpResponseRedirect("/")

def forbidden(request):

    return render_to_response("Error/forbidden.html")


class signin(TemplateView):

    def post(self,request,*args, **kwargs):
        company = Company()

        username = request.POST.get('username')
        password = request.POST.get('password')

        if company.validate_signin(username,password):
            Session().do_login(username)
            response = HttpResponse(status=200)
            set_cookie(response, 'userId', username)
            return response
        else:
            return HttpResponse(status=401)

class signup(TemplateView):

    def post(self,request,*args, **kwargs):
        diccionario={}

        company = Company()

        username = request.POST.get('username')

        if company.username_exist(username):
            diccionario['msg'] = 'USEREXIST'
            return HttpResponse(json.dumps(diccionario),content_type='application/json')
        else:
            password = request.POST.get('password')
            email = request.POST.get('email')
            companyname = request.POST.get('companyname')
            company.create(username=username,companyName = companyname, email=email, password=password)
            diccionario['msg'] = 'OK'
        return HttpResponse(json.dumps(diccionario),content_type='application/json')