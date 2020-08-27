from django.db import models
from django import forms
from django.forms import ModelForm
from django.core.files.base import File
from django.db.models import CharField, Model
from datetime import datetime
from django.utils import timezone

#adding a comment
class File(models.Model):
    file = models.FileField(blank=False, null=False)
    author = models.CharField(max_length=141,default="Admin")
    subject = models.CharField(max_length=101)
    year = models.IntegerField()
    resourceType = models.CharField(max_length=20, blank=True, null=True)
    semester = models.IntegerField()
    numberofUpvotes = models.IntegerField(default=0)
    numberofDownvotes = models.IntegerField(default=0)
    created = models.DateTimeField(default=timezone.now)
    verified = models.BooleanField(default=False)

class Interview(models.Model):
    name = models.CharField(max_length=141)
    title = models.CharField(max_length=101)
    yearPlaced = models.IntegerField()
    experience = models.CharField(max_length=2000, blank=True, null=True)
    yearPassout = models.IntegerField()
    company = models.CharField(max_length=20,default="")
    numberofUpvotes = models.IntegerField(default=0)
    created = models.DateTimeField(default=timezone.now)
    verified = models.BooleanField(default=False)

class Login(models.Model):
    username  =  models.CharField(max_length=20)
    EmailId   =  models.EmailField(max_length=100)
    role      =  models.CharField(max_length=10,default="student")
    password =   models.CharField(max_length=32)
    rollNumber=  models.CharField(max_length=10, primary_key = True)

    def __str__(self):
        return self.file.name

    def __str__(self):
        return self.name

    def __str__(self):
        return self.username

class CommentsPYQ(models.Model):
    author = models.CharField(max_length=20)
    commentBody = models.CharField(default="", max_length=1000)
    pyq = models.ForeignKey(File, default=None, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.author

class CommentsExp(models.Model):
    author = models.CharField(max_length=20)
    commentBody = models.CharField(default="", max_length=1000)
    exp = models.ForeignKey(Interview, default=None, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.author        
