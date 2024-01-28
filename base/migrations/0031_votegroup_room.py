# Generated by Django 4.2.6 on 2024-01-25 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0030_profile_votegroup_chat_participants'),
    ]

    operations = [
        migrations.AddField(
            model_name='votegroup',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.chat'),
        ),
    ]
