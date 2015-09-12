from django.shortcuts import  HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt



import json

def singout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/")


class singin(TemplateView):
    def post(self,request,*args, **kwargs):
        diccionario={}
        print("entro")
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            diccionario['msg'] = 'OK'
            print("login")
            return HttpResponse("/competition/")
        else:
            print('no login')
            diccionario['msg'] = 'error'
            # Show an error page
            HttpResponse(json.dumps(diccionario),content_type='application/json')