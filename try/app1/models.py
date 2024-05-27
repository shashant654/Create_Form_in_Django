from django.db import models

class StudentModel(models.Model):
          name = models.CharField(max_length=50)
          city = models.CharField(max_length=100)
          marks = models.IntegerField()


# Create your models here.
