from django.db import models
from .constants import STATUS_CHOICES, DIFFICULTY_CHOICES

class ProblemCategory(models.Model):
	name = models.CharField(max_length=255)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural='Problem Categories'

class Tutorial(models.Model):
	name = models.CharField(max_length=255)
	difficulty = models.IntegerField(choices=DIFFICULTY_CHOICES, default=1)
	details = models.TextField(blank=True, null=True, default='')
	category = models.ForeignKey(ProblemCategory)
	status = models.IntegerField(choices=STATUS_CHOICES, default=1)
	link_to_material = models.URLField()

	def __unicode__(self):
		return self.name

class ProblemSource(models.Model):
	name = models.CharField(max_length=255)

	def __unicode__(self):
		return self.name

class Problem(models.Model):
	name = models.CharField(max_length=255)
	difficulty = models.IntegerField(choices=DIFFICULTY_CHOICES, default=1)
	details = models.TextField(blank=True, null=True, default='')
	source = models.ForeignKey(ProblemSource)
	category = models.ForeignKey(ProblemCategory)
	status = models.IntegerField(choices=STATUS_CHOICES, default=1)	
	link_to_material = models.URLField()

	def __unicode__(self):
		return self.name

class TrainingSession(models.Model):
	session_name = models.CharField(max_length=255)
	tutorial = models.ForeignKey(Tutorial)
	problem_1 = models.ForeignKey(Problem, related_name='Problem 1')
	problem_2 = models.ForeignKey(Problem, blank=True, null=True, related_name='Problem 2')
	problem_3 = models.ForeignKey(Problem, blank=True, null=True, related_name='Problem 3')
	completed = models.BooleanField(default=False)
	completed_on = models.DateField(blank=True, null=True)
	comments = models.TextField(blank=True, null=True)

	def __unicode__(self):
		return self.session_name






