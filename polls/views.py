from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse

# Create your views here.
def index(request):
    questions = Question.objects.all()
    context = {'questions':questions}
    return render(request,'polls/index.html', context)
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question' : question}
    return render(request, 'polls/detail.html', context)
def result(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    context = {'question' : question}
    return render(request,'polls/result.html', context)
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice = Choice.objects.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {'question':question, 'error_message':'You did not select a choice.'}
        return render(request, 'polls/detail.html',context)
    else:
        choice.votes = F('votes') + 1
        choice.save()
        return HttpResponseRedirect(reverse('polls:result', args=(question_id,)))