from dataclasses import fields
import imp
from django.db import models
from django import forms

# Create your models here.

# example of modelform inheritance 

class User(models.Model):
    student_name=models.CharField(max_length=22)
    teacher_name=models.CharField(max_length=22)
    email=models.EmailField(max_length=22)
    password=models.CharField(max_length=22)



