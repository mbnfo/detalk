# Generated by Django 4.2.6 on 2023-11-11 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_alter_bids_seen'),
    ]

    operations = [
        migrations.AddField(
            model_name='bids',
            name='note',
            field=models.CharField(max_length=1250, null=True),
        ),
    ]
