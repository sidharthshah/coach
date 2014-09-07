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


