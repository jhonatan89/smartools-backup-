from django.shortcuts import render_to_response, RequestContext

# Create your views here

def index(request):
    return render_to_response('Home/index.html', context=RequestContext(request))