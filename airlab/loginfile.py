from django.db import models

class Login(models.Model):
    email = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100 , default=None)
    lastname = models.CharField(max_length=100 , default=None) 
    location = models.CharField(max_length=100 , default=None)
    type = models.CharField(max_length=100 , default=None)
    password = models.CharField(max_length=100)
    terms = models.BooleanField(default=None)