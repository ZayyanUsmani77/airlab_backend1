# Generated by Django 4.1.5 on 2023-02-20 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airlab', '0021_booklab_service_status_lab_lab_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='lab_image',
            field=models.ImageField(default=None, upload_to='my_file'),
        ),
        migrations.AlterField(
            model_name='lab',
            name='lab_url',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]
