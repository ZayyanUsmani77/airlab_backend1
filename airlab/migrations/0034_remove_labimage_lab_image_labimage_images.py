# Generated by Django 4.1.5 on 2023-02-22 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airlab', '0033_alter_labimage_lab_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='labimage',
            name='lab_image',
        ),
        migrations.AddField(
            model_name='labimage',
            name='images',
            field=models.FileField(default=None, upload_to=''),
        ),
    ]
