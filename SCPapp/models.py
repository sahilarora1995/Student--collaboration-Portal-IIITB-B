from django.db import models
from django.core.files.base import File
from django.db.models import CharField, Model

class File(models.Model):
    file = models.FileField(blank=False, null=False)
    subject = models.CharField(max_length=101)
    year = models.IntegerField(default=0)
    resourceType = models.CharField(max_length=20, blank=True, null=True)
    semester = models.IntegerField(default=0)
    numberofUpvotes = models.IntegerField(default=0)
    numberofDownvotes = models.IntegerField(default=0)


    def __str__(self):
        return self.file.name