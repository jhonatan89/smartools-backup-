import json

from django.shortcuts import  HttpResponseRedirect,HttpResponse,render_to_response
from django.contrib import auth
#from session import Session
from django.contrib.auth.models import User, Group
from django.views.generic import TemplateView
#from cloudProject.applications.MongoDB_APP.Company import Company


def signout(request):

    auth.logout(request)

    return HttpResponseRedirect("/")

def forbidden(request):

    return render_to_response("Error/forbidden.html")


class signin(TemplateView):

    def post(self,request,*args, **kwargs):
        diccionario={}
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=401)
        # company = Company()
        #
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        #
        # if company.validate_signin(username,password):
        #     print "antes" + username
        #     Session().do_login(username)
        #     print "guardo"
        #     return HttpResponse(status=200)
        # else:
        #     return HttpResponse(status=401)

class signup(TemplateView):

    def post(self,request,*args, **kwargs):

        diccionario={}

        username = request.POST.get('username')

        if User.objects.filter(username=username).exists():

            diccionario['msg'] = 'USEREXIST'

            return HttpResponse(json.dumps(diccionario),content_type='application/json')
        else:

            password = request.POST.get('password')
            email = request.POST.get('email')
            first_name = request.POST.get('companyname')

            user = User.objects.create_user(username=username, email=email, password=password,first_name=first_name)

            group = Group.objects.get(name='Company')

            user.groups.add(group)
            user.is_staff=True
            user.save()
            user = auth.authenticate(username=username, password=password)

            auth.login(request, user)
            diccionario['msg'] = 'OK'
            return HttpResponse(json.dumps(diccionario),content_type='application/json')



        # diccionario={}
        #
        # company = Company()
        #
        # username = request.POST.get('username')
        #
        # if company.username_exist(username):
        #     diccionario['msg'] = 'USEREXIST'
        #     return HttpResponse(json.dumps(diccionario),content_type='application/json')
        # else:
        #     password = request.POST.get('password')
        #     email = request.POST.get('email')
        #     companyname = request.POST.get('companyname')
        #     company.create(username=username,companyName = companyname, email=email, password=password)
        #     diccionario['msg'] = 'OK'
        # return HttpResponse(json.dumps(diccionario),content_type='application/json')