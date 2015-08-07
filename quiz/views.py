# coding: utf-8

from django.shortcuts import render
from quiz.models import Quiz

# Create your views here.

def startpage(request):
	context ={
		"quizzes": Quiz.objects.all(),
	}
	return render(request, "quiz/startpage.html", context)
def quiz(request, slug):
	context = {
		"quiz": quizzes[slug],
		"quiz_slug": slug,
	}
	return render(request, "quiz/quiz.html", context)

def question(request, slug, number):
	context = {
		"question_number": number,
	    "question": u"	This is Kathrine Switzer. Which marathon did she become the first woman to complete as a registered participant in 1967, five years before women were officially allowed to enter?",
		"answer1": u"Boston Marathon",
	   	"answer2": u"London Marathon",
	    "answer3": u"New York City Marathon",
	    "quiz_slug": slug,
	}
	return render(request, "quiz/question.html", context)

def completed(request, slug):
	context = {
	    "correct": 12,
	    "total": 20,
		"quiz_slug": slug,
	}
	return render(request, "quiz/completed.html", context)








