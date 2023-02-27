from django.db import models

class ContactLab(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_email = models.CharField(max_length=100 , default=None)
    contact_phone = models.CharField(max_length=100 , default=None) 
    contact_lab_date = models.DateField()
    contact_enquiry = models.CharField(max_length=300 , default=None)