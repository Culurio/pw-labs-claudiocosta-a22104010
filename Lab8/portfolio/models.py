from django.db import models

# Create your models here.
class Cadeira(models.Model):
    def __init__(self,name,year,etcs,semester,school_year,ranking,topics,teacher):
        self.name = name
        self.year = year
        self.etcs = etcs
        self.semester = semester
        self.school_year = school_year
        self.ranking = ranking
        self.topics = topics
        self.teacher = teacher

    name = models.CharField(max_length=30)
    year = models.IntegerField(default=0)
    etcs = models.IntegerField(default=0)
    semester = models.IntegerField(default=0)
    school_year = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    topics = models.CharField(max_length=100)

    def __str__(self):
        return f"nome:{self.name}"

class Person():
    def __init__(self,name,linkedin):
        self.name = name
        self.linkedin = linkedin
    def __str__(self):
        return self.name

class Teacher(Person,models.Model):
    def __init__(self, name, uni_url, linkedin):
        super().__init__(name,linkedin)
        self.uni_url = uni_url

    name = models.CharField(max_length=30)
    lusofona_url = models.CharField(max_length=100)
    linkdin = models.CharField(max_length=100)

class Student(Person,models.Model):
    def __init__(self, name,linkedin,portfolio,github):
        super().__init__(name,linkedin)
        self.portfolio = portfolio
        self.github = github

    name = models.CharField(max_length = 30)
    portfolio = models.CharField(max_length = 100)
    github = models.CharField(max_length = 100)
    linkdin = models.CharField(max_length = 100)

class Project():
    def __init__(self,title,description,image,year,subject,participants,github,video_url,tech,skills):
       self.title = title
       self.description = description 
       self.image = image 
       self.year = year 
       self.subject = subject
       self.participants = participants
       self.github = github 
       self.video_url = video_url 
       self.tech = tech 
       self.skills = skills   
    
