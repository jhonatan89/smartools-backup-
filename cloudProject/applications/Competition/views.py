from django.shortcuts import render_to_response, RequestContext,redirect,HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.views.generic import TemplateView

import platform

#Impor auth
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

#Import Models
from cloudProject.applications.Competition.models import Competition

#Import Forms
from cloudProject.applications.Competition.forms import CreateNewCompetition

@login_required
@user_passes_test(lambda u: u.groups.filter(Q(name='Company')), login_url='forbidden')
def index(request):

    try:
        user_id = request.user.id
        company = User.objects.get(id=user_id)
    except:
        company = User.objects.get(id=-1)

    form = CreateNewCompetition()

    competitions_list = Competition.objects.filter(Q(company=company) & Q(active=True))

    paginator = Paginator(competitions_list, 3)

    page = request.GET.get('page')

    try:
        competitions = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        competitions = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        competitions = paginator.page(paginator.num_pages)

    ctx= {'competitions':competitions,'form': form}

    if request.method == 'POST':
        print('post')
        form = CreateNewCompetition(request.POST, request.FILES)
        if form.is_valid():

            print('valid')
            new_competition = Competition(name=request.POST['name'],
                                          image=request.FILES['image'],
                                          description=request.POST['description'],
                                          url='url',
                                          active=True,
                                          company=company)
            new_competition.save(form)
            new_competition.url="http://" + platform.node() + ":8000/competitions/" + str(new_competition.id)
            new_competition.save()

            return HttpResponseRedirect("/competitions")

    return render_to_response('Competition/index.html', ctx, context_instance=RequestContext(request))

class finish(TemplateView):

    def post(self,request,id_competition):

        c = Competition.objects.get(id=id_competition)
        c.active = False
        c.save()

        return HttpResponseRedirect("/competitions")





