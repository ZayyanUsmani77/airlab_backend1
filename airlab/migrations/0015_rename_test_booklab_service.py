# Generated by Django 4.1.5 on 2023-02-14 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('airlab', '0014_rename_airport_pickup_booklab_payment_method_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booklab',
            old_name='test',
            new_name='service',
        ),
    ]
