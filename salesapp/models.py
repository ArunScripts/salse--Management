from django.contrib.auth.models import User
from django.db import models



# Create your models here.

class Student(models.Model):
    salse_person=models.ForeignKey(User,null=True,blank=True,on_delete=models.SET_NULL)
    date_of_join=models.DateField()
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    age=models.IntegerField()
    place=models.CharField(max_length=100)
    education=models.CharField(max_length=200)
    skills=models.CharField(max_length=200)


    def __str__(self):
        return self.name





