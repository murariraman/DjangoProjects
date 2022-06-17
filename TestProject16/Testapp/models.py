from django.db import models
# creating models for student class


# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    password=models.CharField(max_length=20)

