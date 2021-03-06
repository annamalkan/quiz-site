from django.db import models

# Create your models here.
class Quiz(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100)
	description = models.TextField()
	def __unicode__(self):
		return self.name

class Question(models.Model):
	quiz = models.ForeignKey(Quiz, related_name="questions")
	question = models.TextField()
	image_link = models.CharField(max_length=100, default="/static/photos/default-image.jpg")
	#image = models.ImageField(upload_to="/static/photos/", default="/static/photos/default-image.jpg")
	answer1 = models.CharField(max_length=100)
	answer2 = models.CharField(max_length=100)
	answer3 = models.CharField(max_length=100)
	answerinfo = models.TextField()
	correct = models.PositiveIntegerField()

	def __unicode__(self):
		return self.quiz.name + "/ " + self.question

