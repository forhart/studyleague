from django.db import models
from django.contrib import admin

# Create your models here.

class Stream(models.Model):
    title = models.CharField(max_length=60,unique=True)
    description = models.TextField(blank=True)

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
    Semester_name = models.CharField(max_length=4, choices = SEMESTER_CHOICES,unique=True)

    def __unicode__(self):
        return self.Semester_name

class Subject(models.Model):
    title = models.CharField(max_length=60,unique=True)
    description = models.TextField(blank=True)
    
    streams = models.ManyToManyField(Stream)
    semester = models.ForeignKey(Semester)
    def __unicode__(self):
        return self.title

