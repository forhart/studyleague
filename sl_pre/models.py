from django.db import models
from django.contrib import admin
from ckeditor.fields import RichTextField
from django.forms import extras
from django import forms
#import settings
 #for date of birth field
# Create your models here.


class Stream(models.Model):
    title = models.CharField(max_length=60,unique=True)
    slug = models.SlugField(max_length=60,unique=True)
    description = RichTextField(blank=True)

    def __unicode__(self):
        return self.title 



class Student(models.Model):
    GENDER_CHOICES = (
        (u'M',u'Male'),
        (u'F',u'Female')
        )
    first_name    = models.CharField(max_length=60)
    last_name     = models.CharField(max_length=60)
    date_of_birth = forms.DateField(widget=extras.SelectDateWidget)
    email         = models.EmailField(max_length=254)
    age           = models.IntegerField()
    gender        = models.CharField(max_length=2, choices = GENDER_CHOICES)
    home_town     = models.CharField(max_length=100)
    current_city  = models.CharField(max_length=100)
    phone_number  = models.IntegerField(max_length=10)
    college_name  = models.CharField(max_length= 200,blank=True)
    stream        = models.ForeignKey(Stream)
#    address       = models.TextField(max_length=500)
    about_myself  = models.TextField(blank=True)
    hobbies       = models.TextField(blank=True)

    #user may not have twitter of facebook id. so keep these options as non mandatory
    facebook_id   = models.CharField(max_length=100,blank=True)
    twitter_id    = models.CharField(max_length=100,blank=True)
    
#    your_pic      = models.ImageField(upload_to= settings.MEDIA_ROOT)

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


#Subject Model begins here
    
class Subject(models.Model):
    title = models.CharField(max_length=60,unique=True)
    slug = models.SlugField(max_length=60,unique=True)
    description = RichTextField(blank=True)
    streams = models.ManyToManyField(Stream)
    semester = models.ForeignKey(Semester)
    syllabus = models.FileField(upload_to="/syllabus/",blank=True)
    def __unicode__(self):
        return self.title

    def numOfChapters(self):
        return self.chapter_set.count()


class SubjectTestPaper(models.Model):
    title   = models.CharField(max_length=100)
    slug    = models.SlugField(max_length=100)
    link    = models.TextField(blank = True)
    subject = models.ForeignKey(Subject)

class SubjectUpdate(models.Model):
    title = models.CharField(max_length=100)
    slug  = models.SlugField(max_length=100)
    description = models.TextField()
    #foreign_key 
    subject = models.ForeignKey(Subject)
    #modifield content of the subject needs to be linked here .... some logic missing 
#Subject Model Ends here

class Chapter(models.Model):
    title = models.CharField(max_length=100)
    slug  = models.SlugField(max_length=100)
    description = RichTextField(blank=True)
    subject = models.ForeignKey(Subject)

    def __unicode__(self):
        return self.title

#    def numOfSubChapters(self):
#        return self.subchapter_set.count()

    def numOfTopics(self):
        return self.topic_set.count()

#Topic Section begins here 
class Topic(models.Model):
    title = models.CharField(max_length=100)
    slug  = models.SlugField(max_length=100)
    description = RichTextField(blank=True)
    
    chapter = models.ForeignKey(Chapter)

    def __unicode__(self):
        return self.title

class TopicTheory(models.Model):
    title = models.CharField(max_length=100)
    slug  = models.CharField(max_length=100)
    link = models.TextField(blank=True)

    topic = models.ForeignKey(Topic)


class TopicSolved(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    link = models.TextField(blank=True)
    topic = models.ForeignKey(Topic)

class TopicUnsolved(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    link = models.TextField(blank = True)
    
    topic  = models.ForeignKey(Topic)

class TopicVideo(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    link = models.TextField()
    
    topic = models.ForeignKey(Topic)
    

    
class Test(models.Model):
    pass

class Question(models.Model):
    pass





               
class price(models.Model):
    pass
