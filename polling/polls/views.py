from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

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
    try:
        question = Poll.objects.get(uid=question_id)
    except Poll.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    try:
        question = Poll.objects.get(uid=question_id)
    except Poll.DoesNotExist:
        raise Http404("Question does not exist")
    try:
        selected_choice = question.choices
        for choice in question.choices:
            if choice.uid == int(request.POST['choice']):
                selected_choice = choice
    except (KeyError):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.uid,)))

