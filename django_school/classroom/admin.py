from django.contrib import admin
from .models import Profile, Subject,  Student, Equipe, Quiz



# Register your models here.

admin.site.register(Profile)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Equipe)
admin.site.register(Quiz)