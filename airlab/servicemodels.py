from django.db import models

class Service(models.Model):
    
    lab_id = models.IntegerField(default=0)
    new_category = models.CharField(default=None, max_length=100)
    service_category = models.CharField(default=None, max_length=100)
    new_service = models.CharField(default=None, max_length=100)
    select_service = models.CharField(default=None, max_length=100)
    test_name = models.CharField(default=None, max_length=100)
    test_method = models.CharField(default=None, max_length=100)
    electronic = models.BooleanField(default=None)
    papers = models.BooleanField(default=None)
    test_request_form = models.FileField(blank=True , upload_to="my_file")
    service_date = models.DateField(default=None)
    other_method_for_result = models.CharField(default=None, max_length=100)
    listing_type = models.CharField(default=None, max_length=100)
    service_price = models.CharField(default=None, max_length=100)
    listing_description = models.CharField(default=None,  max_length=100)
    addtional_lab_services = models.CharField(default=None, max_length=100)
    service_image = models.FileField(default=None , upload_to="my_file")