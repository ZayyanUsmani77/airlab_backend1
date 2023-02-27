from django.db import models

# Create your models here.

class Signup(models.Model):
    email = models.CharField(default=None, max_length=100)
    firstname = models.CharField(default=None, max_length=100)
    lastname = models.CharField(default=None, max_length=100)
    signup_location = models.CharField(default=None, max_length=100)
    signup_type = models.CharField(default=None, max_length=100)
    password = models.CharField(default=None, max_length=100)
    termsNConditions = models.BooleanField(default=False)
