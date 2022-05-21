from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Person(models.Model):

    name = models.CharField(max_length=50)
    linkdin = models.URLField()
    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Teacher(Person,models.Model):
    lusofona_url = models.URLField()

class Student(Person,models.Model):

    portfolio = models.URLField()
    github = models.URLField()

class Project(models.Model):

    title = models.CharField(max_length=50,default='')
    description = models.CharField(max_length=500)
    #image = models.ImageField()
    year = models.IntegerField(default=0)
    github = models.URLField()
    video_url = models.URLField()
    tech = models.URLField()
    skills = models.CharField(max_length=500)
    participants = models.ForeignKey(Student, on_delete=models.CASCADE)

class Subject(models.Model):

    name = models.CharField(max_length=30)
    year = models.IntegerField(default=0)
    etcs = models.IntegerField(default=0)
    semester = models.IntegerField(default=0)
    school_year = models.IntegerField(default=0)
    rank = models.IntegerField(default=0, validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ])
    topics = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, blank = True)
    teacher = models.ManyToManyField(Teacher, blank = True)
    #subject_project = models.OneToOneField(Project,on_delete=models.CASCADE,primary_key=True,)

    def __str__(self):
        return self.name


        
    
