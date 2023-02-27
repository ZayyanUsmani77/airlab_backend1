# Generated by Django 4.1.5 on 2023-02-14 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('airlab', '0013_rename_connote_booklab_sample_tracking_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booklab',
            old_name='airport_pickup',
            new_name='payment_method',
        ),
        migrations.RemoveField(
            model_name='booklab',
            name='breakfast',
        ),
        migrations.RemoveField(
            model_name='booklab',
            name='card_cvv',
        ),
        migrations.RemoveField(
            model_name='booklab',
            name='card_expiration',
        ),
        migrations.RemoveField(
            model_name='booklab',
            name='card_number',
        ),
        migrations.RemoveField(
            model_name='booklab',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='booklab',
            name='payment_with',
        ),
        migrations.RemoveField(
            model_name='booklab',
            name='paymnent_card_type',
        ),
    ]
