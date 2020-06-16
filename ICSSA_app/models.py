from django.db import models
from django.utils import timezone
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
import random
import string
from .managers import StudentManager, LevelManager
# Create your models here.

POLL_STATUS = [('active', 'Active'), ('inactive', 'Inactive'), ('old', 'Old')]

class Level(models.Model):
	name = models.CharField(max_length=5)

	objects = LevelManager()

	class Meta:
		unique_together = [['name']]

	def natural_key(self):
		return (self.name)

	def __str__(self):
		return self.name

class Student(models.Model):
	is_president = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	email = models.EmailField(unique=True)
	access_code = models.CharField(max_length=10, editable=False)
	first_name = models.CharField(max_length=30, default='')
	last_name = models.CharField(max_length=30, default='')
	matric_number = models.CharField(max_length=12, unique=True)
	level = models.ForeignKey(Level, on_delete=models.CASCADE)
	phone_number = models.CharField(max_length=15, default='')
	date_created = models.DateTimeField(editable=False)

	objects = StudentManager()

	class Meta:
		ordering = ['matric_number']

	def save(self, *args, **kwargs):
		if not self.id:
			self.date_created = timezone.now()
			characters = string.ascii_uppercase + string.digits
			self.access_code = ''.join(random.choice(characters) for i in range(7))
		super(Student, self).save(*args, **kwargs)

	def __str__(self):
		return "{} {}, {}".format(self.first_name, self.last_name, self.matric_number)


class DepartmentalInfo(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()

	def __str__(self):
		return self.title

class ExecutiveTenure(models.Model):
	year = models.PositiveSmallIntegerField()
	title = models.CharField(max_length=100)
	is_active = models.BooleanField(default=False)

	def __str__(self):
		return str(self.year) + " " + self.title

class ExecutivePost(models.Model):
	title = models.CharField(max_length=30)

	def __str__(self):
		return self.title


class ExecutiveMember(models.Model):
	member = models.ForeignKey(Student, on_delete=models.CASCADE)
	tenure = models.ForeignKey(ExecutiveTenure, on_delete=models.CASCADE)
	post = models.ForeignKey(ExecutivePost, on_delete=models.CASCADE)

	def __str__(self):
		return "{}, {}".format(self.post.title, str(self.tenure.year))


class PollQuestion(models.Model):
	level = models.ForeignKey(Level, on_delete=models.CASCADE)
	question = models.TextField()
	running_hours = models.CharField(max_length=15)
	status = models.CharField(choices=POLL_STATUS, max_length=15, default='inactive')

	def __str__(self):
		return self.question

class PollChoice(models.Model):
	poll = models.ForeignKey(PollQuestion, on_delete=models.CASCADE)
	choice = models.CharField(max_length=100, default='')

	def __str__(self):
		return "{}, {}".format(self.choice, self.poll.question)

class PollParticipant(models.Model):
	poll = models.ForeignKey(PollQuestion, on_delete=models.CASCADE)
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	choice = models.ForeignKey(PollChoice, on_delete=models.CASCADE)

	def __str__(self):
		return "{}, {}".format(self.student.matric_number, self.poll.question)
