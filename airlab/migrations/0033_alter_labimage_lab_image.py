# Generated by Django 4.1.5 on 2023-02-22 06:50

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airlab', '0032_alter_labimage_lab_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labimage',
            name='lab_image',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.ImageField(upload_to='images/'), blank=True, null=True, size=None),
        ),
    ]
