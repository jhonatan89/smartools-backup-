from datetime import datetime

from django.shortcuts import render_to_response, RequestContext, HttpResponseRedirect
from django.db.models import Q
from django.utils.timezone import utc
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.core.mail import send_mail
from django.views.generic import TemplateView


#Impor auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

#Import Models
from cloudProject.applications.Competition.models import Competition

#Import Forms
from cloudProject.applications.Competition.forms import CreateNewCompetition


@login_required(login_url='/account/forbbiden/')
def index(request):

    try:
        user_id = request.user.id
        company = User.objects.get(id=user_id)
    except:
        company = User.objects.get(id=-1)

    form = CreateNewCompetition()

    competitions_list = Competition.objects.filter(Q(company=company) & Q(active=True))

    paginator = Paginator(competitions_list, 50)

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
        print request.POST['name']
        print request.FILES['image']
        print request.POST['description']
        print request.POST.get('startDate')
        print request.POST.get('endDate')
        form = CreateNewCompetition(request.POST, request.FILES)
        #if form.is_valid():
        print (request.POST.get('startDate'))
        print('valid')
        new_competition = Competition(name=request.POST['name'],
                                      image=request.FILES['image'],
                                      description=request.POST['description'],
                                      startDate=request.POST.get('startDate'),
                                      endDate=request.POST.get('endDate'),
                                      url='url',
                                      active=True,
                                      company=company)
        new_competition.save(form)
        new_competition.url="/competitions/" + str(new_competition.id)
        new_competition.save()

        ctx['resp'] = 'OK'

        return HttpResponseRedirect("/competitions")
        #else:
         #   ctx['resp'] = 'BAD'
          #  print form.is_valid
    return render_to_response('Competition/index.html', ctx, context_instance=RequestContext(request))

class finish(TemplateView):

    def post(self,request,id_competition):

        c = Competition.objects.get(id=id_competition)
        c.endDate=datetime.utcnow().replace(tzinfo=utc)
        c.active = False
        c.save()

        return HttpResponseRedirect("/competitions")

class edit(TemplateView):

    def post(self,request,id_competition):

        c = Competition.objects.get(id=id_competition)
        c.name = request.POST['nameedit']
        c.description = request.POST['descriptionedit']
        c.save()

        send_mail('Competition changed', 'Your competition' + id_competition + 'has been changeg .', 'smarttoolssaas@example.com',[request.user.email], fail_silently=False)

        return HttpResponseRedirect("/competitions")




