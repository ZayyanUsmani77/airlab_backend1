# Generated by Django 4.1.5 on 2023-02-14 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airlab', '0017_booklab_packaging_booklab_packaging_details_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booklab',
            name='amount_paid',
            field=models.CharField(default=None, max_length=100),
        ),
    ]