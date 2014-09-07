from django.contrib import admin
from .models import ProblemCategory, Tutorial, ProblemSource, Problem, TrainingSession

admin.site.register(ProblemCategory)
admin.site.register(Tutorial)
admin.site.register(ProblemSource)
admin.site.register(Problem)
admin.site.register(TrainingSession)
