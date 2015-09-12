from django.shortcuts import render_to_response, RequestContext

def index(request):
    return render_to_response('Competition/index.html', context=RequestContext(request))

# Create your views here.
