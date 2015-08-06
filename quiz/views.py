# coding: utf-8

from django.shortcuts import render
quizzes = {
	"klassiker": {
   		"name": u"Political heroes",
	   	"description": u"Hur bra kan du dina klassiker?"
	},
	"fotboll": {
	   	"name": u"Sports stars",
	   	"description": u"How many of these spectacular sportswomen are you familiar with? Find out and learn more about all of them by completing this quiz!"
	},
	"kanda-hackare": {
	    	"name": u"Scientific masterminds",
	    	"description": u"Hackerhistoria är viktigt, kan du den?"	},
}


# Create your views here.

def startpage(request):
	context ={
		"quizzes":quizzes,
	}
	return render(request, "quiz/startpage.html", context)
def quiz(request, slug):
	context = {
		"quiz": quizzes[slug],
		"quiz_slug": slug,
	}
	return render(request, "quiz/quiz.html", context)
def question(request):
	return render(request, "quiz/question.html")
def completed(request):
	return render(request, "quiz/completed.html")