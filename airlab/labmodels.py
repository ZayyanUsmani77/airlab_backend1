from django.db import models

class Lab(models.Model):
    email = models.CharField(default=None, max_length=100)
    lab_type = models.CharField(default=None, max_length=100)
    accreditation = models.BooleanField(default=False)
    lab_status = models.CharField(default=None, max_length=100) # pending, approve, reject
    service_list =  models.JSONField(
        default={
            'certification': None,
            'consulting': None,
            'testing': None,
            'manufacturing': None,
            'rnd': None,
            'inspection': None,
            'whitelab': None,
        }
    )
    address1 = models.CharField(default=None, max_length=100)
    # address2 = models.CharField(default=None, max_length=100)
    city = models.CharField(default=None, max_length=100)
    state = models.CharField(default=None, max_length=100)
    country = models.CharField(default=None, max_length=100)
    xcoordinate = models.CharField(default=None, max_length=100)
    ycoordinate = models.CharField(default=None, max_length=100)
    lab_name = models.CharField(default=None, max_length=100)
    lab_description = models.CharField(default=None, max_length=1000)
    lab_visibility = models.CharField(default=None, max_length=100)
    home_test = models.BooleanField(default=False)
    open_for_collaborations = models.BooleanField(default=False)
    lab_url = models.CharField(default=None, max_length=100)
    lab_image = models.FileField(default=None , upload_to="my_file")
    logo = models.FileField(default=None , upload_to="my_file")
    rating = models.FloatField(default=None)
    courier = models.BooleanField(default=False)
