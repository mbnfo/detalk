# Generated by Django 4.2.6 on 2024-01-28 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0044_chat_includevotes'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='link',
            field=models.CharField(blank=True, default='this person doesnt have any links', max_length=250, null=True),
        ),
    ]
