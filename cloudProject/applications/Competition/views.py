from django.shortcuts import render_to_response, RequestContext
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

#Impor auth
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

#Import Models
from cloudProject.applications.Competition.models import Competition

#def index(request):
#    return render_to_response('Competition/index.html', context=RequestContext(request))

@login_required
@user_passes_test(lambda u: u.groups.filter(Q(name='Company')), login_url='Home/index')
def index(request):

    if request.method == 'GET':

        try:
            user_id = request.user.id
            company = User.objects.get(id=user_id)
            print()

        except:
            company = User.objects.get(id=-1)

        competitions_list = Competition.objects.filter(Q(company=company) & Q(active=True))

        paginator = Paginator(competitions_list, 1)
        page = request.GET.get('page')

        try:
            competitions = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            competitions = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            competitions = paginator.page(paginator.num_pages)

        print(company)

        ctx= {'competitions':competitions}

    return render_to_response('Competition/index.html', ctx, context_instance=RequestContext(request))





