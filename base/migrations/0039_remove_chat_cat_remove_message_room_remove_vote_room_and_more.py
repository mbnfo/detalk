# Generated by Django 4.2.6 on 2024-01-26 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0038_remove_chat_participants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='cat',
        ),
        migrations.RemoveField(
            model_name='message',
            name='room',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='room',
        ),
        migrations.RemoveField(
            model_name='votegroup',
            name='room',
        ),
        migrations.RemoveField(
            model_name='votegroup',
            name='voted_users',
        ),
        migrations.RemoveField(
            model_name='votegroup',
            name='votes',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Chat',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
        migrations.DeleteModel(
            name='VoteGroup',
        ),
    ]
