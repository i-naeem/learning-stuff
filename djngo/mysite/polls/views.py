from django.http import HttpResponse
from django.shortcuts import render
from .models import Question


def index(request):
    latest_polls = Question.objects.order_by('-pub_date')[:5]
    context = {
        "latest_polls": latest_polls
    }

    return render(request, "polls/index.html", context)


def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    return HttpResponse(question.question_text)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
