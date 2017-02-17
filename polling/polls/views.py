from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
import mongoengine
from polls.models import Poll, Choice


def index(request):
    latest_question_list = Poll.objects().all()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Poll.objects.get(uid=question_id)
    except Poll.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

