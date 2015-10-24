from datetime import datetime

from django.shortcuts import render_to_response, RequestContext, HttpResponseRedirect, render
from django.db.models import Q
from django.utils.timezone import utc
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import TemplateView
from cloudProject.applications.Account.session import Session


#Import Models
from cloudProject.applications.MongoDB_APP.Company import Company
from cloudProject.applications.MongoDB_APP.Competition import Competition

# Import Forms
from cloudProject.applications.Competition.forms import CreateNewCompetition


def index(request):
    if Session().verify_current_session(request.COOKIES['userId']):
        print "entro a index"
        company ="ca1"

        form = CreateNewCompetition()

        competitions_list = Company().get_competitions(company)

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
            form = CreateNewCompetition(request.POST, request.FILES)
            #if form.is_valid():
            Competition().create(name=request.POST['name'],
                                      image=request.FILES['image'],
                                      description=request.POST['description'],
                                      startDate=request.POST.get('startDate'),
                                      endDate=request.POST.get('endDate'),
                                      url='url',
                                      active=True)

            ctx['resp'] = 'OK'

            return HttpResponseRedirect("/competitions")
            #else:
             #   ctx['resp'] = 'BAD'
              #  print form.is_valid
        return render_to_response('Competition/index.html', ctx, context_instance=RequestContext(request))
    else:
        print "entro a forbidden"
        return render_to_response("Error/forbidden.html")


class finish(TemplateView):
    def post(self, request, id_competition):
        c = Competition.objects.get(id=id_competition)
        c.endDate = datetime.utcnow().replace(tzinfo=utc)
        c.active = False
        c.save()

        return HttpResponseRedirect("/competitions")


class edit(TemplateView):
    def post(self, request, id_competition):
        c = Competition.objects.get(id=id_competition)
        c.name = request.POST['nameedit']
        c.description = request.POST['descriptionedit']
        c.save()

        # send_mail('Competition changed', 'Your competition' + id_competition + 'has been changeg .', 'smarttoolssaas@example.com',[request.user.email], fail_silently=False)

        return HttpResponseRedirect("/competitions")


def show_all_competitions(request):
    list_competitions = Competition.objects.filter(active=True)
    return render(request, 'Competition/active_competitions.html', {'competitions': list_competitions})
