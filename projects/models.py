from django.db import models

# Create your models here.
class Project(models.Model):
    español = models.CharField(max_length=100)
    ashaninka = models.CharField(max_length=100)
    pronunciacion = models.CharField(max_length=100)