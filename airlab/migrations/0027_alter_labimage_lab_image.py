# Generated by Django 4.1.5 on 2023-02-22 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airlab', '0026_remove_labimage_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labimage',
            name='lab_image',
            field=models.ImageField(default=None, upload_to='my_file'),
        ),
    ]
