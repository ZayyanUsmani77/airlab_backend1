# Generated by Django 4.1.5 on 2023-02-02 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airlab', '0006_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review_lab_id',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_title',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
