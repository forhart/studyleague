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

class SubjectUpdates(models.Model):
    title = models.CharField(max_length=100)
    slug  = models.SlugField(max_length=100)
    description = models.TextField()
    #foreign_key 
    subject = models.ForeignKey(Subject)

#Subject Model Ends here

class Chapter(models.Model):
    title = models.CharField(max_length=100)
    slug  = models.SlugField(max_length=100)
    description = RichTextField(blank=True)
    subject = models.ForeignKey(Subject)

    def __unicode__(self):
        return self.title

    def numOfSubChapters(self):
        return self.subchapter_set.count()

class SubChapter(models.Model):
    title = models.CharField(max_length=100)
    slug  = models.SlugField(max_length=100)
    description = RichTextField(blank=True)
    
    chapter = models.ForeignKey(Chapter)

    def __unicode__(self):
        return self.title

class SubChapterTheory(models.Model):
    title = models.CharField(max_length=100)
    slug  = models.CharField(max_length=100)
    link = models.TextField(blank=True)

    subchapter = models.ForeignKey(SubChapter)


class SubChapterSolved(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    link = models.TextField(blank=True)
    subchapter = models.ForeignKey(SubChapter)

class SubChapterUnsolved(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    link = models.TextField(blank = True)
    
    subchapter = models.ForeignKey(SubChapter)

class SubChapterVideo(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    link = models.TextField()
    
    subchapter = models.ForeignKey(SubChapter)
    
    
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
