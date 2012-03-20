from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from jobs.models import *

def index(request):

  categories = Categories.objects.get_with_jobs()

  import settings
  for category in categories:
    category.active_jobs = Jobs.objects.get_active_jobs_by_category(category, settings.JOB_BY_CATEGORY_LIMIT)

  return render_to_response('index.html', {'categories': categories}, context_instance=RequestContext(request))

def show_job(request, company, id, position, location):
  return HttpResponse("You're looking at the results of job %s." % id)





