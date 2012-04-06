from django.db import models
from django.contrib import admin
from ckeditor.fields import RichTextField
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
    title = models.CharField(max_length=60,unique=True)
    slug = models.SlugField(max_length=60,unique=True)
    description = RichTextField(blank=True)

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
    title  = models.CharField(max_length=8, choices = SEMESTER_CHOICES)
    slug          = models.SlugField(max_length=10,unique=True)

    def __unicode__(self):
        return self.title


class Subject(models.Model):
    title = models.CharField(max_length=60,unique=True)
    description = RichTextField(blank=True)
    slug = models.SlugField(max_length=60,unique=True)
    streams = models.ManyToManyField(Stream)
    semester = models.ForeignKey(Semester)

    def __unicode__(self):
        return self.title

    def numOfChapters(self):
        return self.chapter_set.count()

class Chapter(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField(blank=True)
    slug  = models.SlugField(max_length=100)
    subject = models.ForeignKey(Subject)

    def __unicode__(self):
        return self.title



class SubChapter(models.Model):
    title = models.CharField(max_length=100)
    slug  = models.SlugField(max_length=100)
    description = RichTextField(blank=True)
    
    chapter = models.ForeignKey(Chapter)

    def __unicode__(self):
        return self.title
    
class Test(models.Model):
    pass

class Question(models.Model):
    pass

class Note(models.Model):
    title    = models.CharField(max_length=200)
    content  = RichTextField(blank=True)
    slug     = models.SlugField(max_length=200,unique=True)
    author   = models.ManyToManyField(Author)
    subject  = models.ForeignKey(Subject)
    chapter  = models.ForeignKey(Chapter)
    semester = models.ForeignKey(Semester)
    stream   = models.ManyToManyField(Stream)

    is_free  = models.BooleanField()
    def __unicode__(self):
        return self.title


    class Meta:
        ordering = ["title"]
      #  list_filter = ('author') this won't work in meta class

               
class Plan(models.Model):
    pass
