from django.db import models
from django.contrib import admin

# Create your models here.

class Student(models.Model):
    GENDER_CHOICES = (
        (u'M',u'Male'),
        (u'F',u'Female')
        )
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    age = models.IntegerField()
    gender = models.CharField(max_length=2, choices = GENDER_CHOICES)

    def __unicode__(self):
        return self.first_name +" " + self.last_name


class Author(models.Model):
    GENDER_CHOICES = (
        (u'M',u'Male'),
        (u'F',u'Female')
        )
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    age = models.IntegerField()
    gender = models.CharField(max_length=2, choices = GENDER_CHOICES)

    def __unicode__(self):
        return self.first_name +" " + self.last_name

class Stream(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.title 

class Subject(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.title

class Chapter(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    subject = models.ForeignKey(Subject)

    def __unicode__(self):
        return self.title
    
class Semester(models.Model):
    SEMESTER_CHOICES = (
        (u'I',    u'First'),
        (u'II',   u'Second'),
        (u'III',  u'Third'),
        (u'IV',   u'Fourth'),
        (u'V',    u'Fifth'),
        (u'VI',   u'Sixth'),
        (u'VII',  u'Seventh'),
        (u'VIII', u'Eigth')
        )
    Semester_name = models.CharField(max_length=8, choices = SEMESTER_CHOICES)

    def __unicode__(self):
        return self.Semester_name

class Note(models.Model):
    title    = models.CharField(max_length=200)
    content  = models.TextField(blank=True)

    author   = models.ManyToManyField(Author)
    subject  = models.ForeignKey(Subject)
    chapter  = models.ForeignKey(Chapter)
    semester = models.ForeignKey(Semester)
    stream   = models.ForeignKey(Stream)

    is_free  = models.BooleanField()
    def __unicode__(self):
        return self.title


    class Meta:
        ordering = ["title"]
      #  list_filter = ('author') this won't work in meta class

               
class Plan(models.Model):
    pass
