# Generated by Django 4.2.6 on 2024-01-25 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0028_alter_vote_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='assigned',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vote',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
