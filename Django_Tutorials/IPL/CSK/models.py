# Create your models here.
from django.db import models

class CSKTEAM(models.Model):
   website = models.CharField(max_length = 50)
   mail = models.CharField(max_length = 50)
   name = models.CharField(max_length = 50)
   # phonenumber = models.IntegerField()

   def __str__(self):
      return self.name


class Student(models.Model):
   first_name = models.CharField(max_length=20)
   last_name = models.CharField(max_length=30)

   class Meta:
      db_table = "student"  