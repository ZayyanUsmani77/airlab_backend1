# Generated by Django 4.1.5 on 2023-02-25 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airlab', '0036_lab_courier'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='labimage',
            name='lab_image',
        ),
        migrations.AddField(
            model_name='labimage',
            name='lab_image',
            field=models.ManyToManyField(to='airlab.imagefile'),
        ),
    ]
