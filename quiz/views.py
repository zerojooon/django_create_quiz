import copy
import random
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse


from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Question,Create_Quiz

from django.http import HttpResponse, Http404


def main(request):
    return render(request, 'quiz/main.html')


def index(request):
    question_list = Question.objects.all()
    return render(request, 'quiz/index.html', {'question_list': question_list})
#

def results(request): #question_id를 파라미터로 받는다.
    questions = Question.objects.all()
    selected_choices = []
    # quiz_title=request.POST.get('quiz_title',None)
    for question in questions:
        # print(question.choice_set.get(pk=request.POST.get['choice.id','']))
        # selected_choices += question.choice_set.filter(pk=request.POST.get('choice{{question.pk}}',''))
        selected_choices += question.choice_set.filter(pk=request.POST.get('choice1', ''))
        selected_choices += question.choice_set.filter(pk=request.POST.get('choice2',  ''))
        selected_choices += question.choice_set.filter(pk=request.POST.get('choice3',  ''))
        selected_choices += question.choice_set.filter(pk=request.POST.get('choice4',  ''))
        selected_choices += question.choice_set.filter(pk=request.POST.get('choice5',  ''))
        selected_choices += question.choice_set.filter(pk=request.POST.get('choice6',  ''))
        selected_choices += question.choice_set.filter(pk=request.POST.get('choice7', ''))
        selected_choices += question.choice_set.filter(pk=request.POST.get('choice8',  ''))
        selected_choices += question.choice_set.filter(pk=request.POST.get('choice9',  ''))
        selected_choices += question.choice_set.filter(pk=request.POST.get('choice10',  ''))

    create_quiz = Create_Quiz.objects.create(
        # quiz_title=quiz_title,
        selected_choices1= selected_choices[0],
        selected_choices2=selected_choices[1],
        selected_choices3=selected_choices[2],
        selected_choices4=selected_choices[3],
        selected_choices5=selected_choices[4],
        selected_choices6=selected_choices[5],
        selected_choices7=selected_choices[6],
        selected_choices8=selected_choices[7],
        selected_choices9=selected_choices[8],
        selected_choices10=selected_choices[9],
    )

    return render(request, 'quiz/results.html', {'selected_choices': selected_choices} )



def list(request):
    user_list = User.objects.all()
    return render(request, 'quiz/list.html', {'user_list': user_list})
