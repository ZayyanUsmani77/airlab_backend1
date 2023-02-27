from django.db import models

class LabImage(models.Model):
    lab_image = models.FileField(default=None , upload_to="my_file")
    logo = models.FileField(default=None , upload_to="my_file")