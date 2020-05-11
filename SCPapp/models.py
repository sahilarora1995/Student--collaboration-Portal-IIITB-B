from django.db import models
from django import forms
from django.forms import ModelForm
from django.core.files.base import File
from django.db.models import CharField, Model

class File(models.Model):
    file = models.FileField(blank=False, null=False)
    subject = models.CharField(max_length=101)
    year = models.IntegerField()
    resourceType = models.CharField(max_length=20, blank=True, null=True)
    semester = models.IntegerField()
    numberofUpvotes = models.IntegerField(default=0)
    numberofDownvotes = models.IntegerField(default=0)

class Interview(models.Model):
    name = models.CharField(max_length=101)
    title = models.CharField(max_length=101)
    yearPlaced = models.IntegerField()
    experience = models.CharField(max_length=2000, blank=True, null=True)
    yearPassout = models.IntegerField()
    numberofUpvotes = models.IntegerField(default=0)


class Login(models.Model):
    username  =  models.CharField(max_length=20)
    EmailId   =  models.EmailField(max_length=100)
    role      =  models.CharField(max_length=10)
    password =   models.CharField(max_length=32)
    rollNumber=  models.CharField(max_length=10, primary_key = True)

    def __str__(self):
        return self.file.name

    def __str__(self):
        return self.name

    def __str__(self):
        return self.username