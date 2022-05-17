from django.contrib import admin
from .models import Cadeira, Person, Teacher, Student, Project
# Register your models here.

admin.site.register(Cadeira)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Project)