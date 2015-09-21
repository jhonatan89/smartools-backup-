from django.shortcuts import render_to_response, RequestContext

# Create your views here

def index(request):
    return render_to_response('Home/index.html', context=RequestContext(request))

def forbidden(request):
    return render_to_response('Home/index.html', context=RequestContext(request))

def about_us(request):
    return render_to_response('Home/about_us.html', context=RequestContext(request))