# Generated by Django 4.1.5 on 2023-02-07 06:57

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airlab', '0008_booklab_lab_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='select_service',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None),
        ),
    ]
