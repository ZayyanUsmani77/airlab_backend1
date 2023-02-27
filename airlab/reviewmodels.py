from django.db import models

class Review(models.Model):
    review_lab_id = models.CharField(max_length=100, default=None)
    review_title = models.CharField(max_length=100,  default=None)
    reviewer_name = models.CharField(max_length=100 , default=None)
    reviewer_email = models.CharField(max_length=100 , default=None) 
    reviewer_description = models.CharField(max_length=100 , default=None) 