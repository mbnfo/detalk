# Generated by Django 4.2.6 on 2023-11-04 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_bids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bids',
            name='bids',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='assigned_work',
        ),
        migrations.AddField(
            model_name='bids',
            name='seen',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='reciept',
            name='seen',
            field=models.BooleanField(default=False),
        ),
    ]