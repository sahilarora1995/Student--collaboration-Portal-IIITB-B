from django.db import models
# Create your models here.
import datetime
class MockSchedular(models.Model):
    name = models.CharField("Name", max_length=240)
    email = models.EmailField()
    day = models.DateField(default=datetime.date.today)
    time = models.TimeField()
    about = models.CharField(max_length=20, default='DSA')
    

    def __str__(self):
        return self.name