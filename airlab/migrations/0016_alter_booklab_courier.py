# Generated by Django 4.1.5 on 2023-02-14 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airlab', '0015_rename_test_booklab_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booklab',
            name='courier',
            field=models.CharField(max_length=100),
        ),
    ]