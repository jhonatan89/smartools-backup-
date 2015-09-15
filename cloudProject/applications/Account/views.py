from django.shortcuts import  HttpResponseRedirect,HttpResponse,render_to_response
from django.contrib import auth
from django.contrib.auth.models import User, Group
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt



import json

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
            # Redirect to a success page.
            diccionario['msg'] = 'OK'

            return HttpResponse(json.dumps(diccionario),content_type='application/json')
        else:

            diccionario['msg'] = 'error'
            # Show an error page
            return HttpResponse(json.dumps(diccionario),content_type='application/json')

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



