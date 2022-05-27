from django.contrib import admin
from .models import Subject, Person, Subject, Teacher, Student, Project,Post
# Register your models here.

admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Project)
admin.site.register(Post)