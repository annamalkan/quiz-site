# coding: utf-8

from django.shortcuts import render
from quiz.models import Quiz
from django.shortcuts import redirect
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.

def startpage(request):
	context ={
		"quizzes": Quiz.objects.all(),
	}
	return render(request, "quiz/startpage.html", context)
def quiz(request, slug):
	try:
		quiz = Quiz.objects.get(slug=slug)
	except Quiz.DoesNotExist:
		raise Http404

	context = {
		"quiz": quiz,
	}
	return render(request, "quiz/quiz.html", context)

def question(request, slug, number):
	number = int(number)
	try:
		quiz = Quiz.objects.get(slug=slug)
	except Quiz.DoesNotExist:
		raise Http404

	context = {
		"quiz": quiz,
	}
	

	quiz = Quiz.objects.get(slug=slug)
	questions = quiz.questions.all()
	if request.POST:
		answer= int(request.POST["answer"])
		saved_answers={}
		if quiz.slug in request.session:
			saved_answers=request.session[quiz.slug]
		saved_answers[str(number)]= answer
		request.session[quiz.slug]=saved_answers
		if questions.count() == number:
			return redirect("completed_page", quiz.slug)
		else:
			return redirect("question_page", quiz.slug, number +1)

	question = questions[number - 1]
	#image = question.image
	context = {
		"question_number": number,
	    "question": question.question,
	    "image_link": question.image_link,
	   	"answer1": question.answer1,
	   	"answer2": question.answer2,
	    "answer3": question.answer3,
	    "quiz": quiz,
	    "answerinfo": question.answerinfo,
	}

	if number > questions.count():
		raise Http404	
	return render(request, "quiz/question.html", context)

def completed(request, slug):
	try:
		quiz = Quiz.objects.get(slug=slug)
	except Quiz.DoesNotExist:
		raise Http404
	questions=quiz.questions.all()
	saved_answers=request.session[slug]
	num_correct_answers=0
	for counter, question in enumerate(questions):
		if question.correct==saved_answers[str(counter+1)]:
			num_correct_answers+=1

	context = {
	    "correct": num_correct_answers,
	    "total": questions.count(),
		"quiz_slug": quiz,
		"questions": questions,
	}
	return render(request, "quiz/completed.html", context)

def handler404(request):
    response = render_to_response('404.html', {},
            context_instance=RequestContext(request))
    response.status_code = 404
    return response






