# Generated by Django 4.2.6 on 2023-11-01 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='job_type',
        ),
    ]