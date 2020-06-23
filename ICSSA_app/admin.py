from django.contrib import admin
from .models import (Student, Level,
                     DepartmentalInfo, ExecutiveTenure,
                     ExecutivePost, ExecutiveMember,
                     PollQuestion, PollChoice, PollParticipant)

# Register your models here.
admin.site.register(Student)
admin.site.register(Level)
admin.site.register(DepartmentalInfo)
admin.site.register(ExecutiveTenure)
admin.site.register(ExecutivePost)
admin.site.register(ExecutiveMember)
admin.site.register(PollQuestion)
admin.site.register(PollChoice)
admin.site.register(PollParticipant)
