# Generated by Django 4.2.6 on 2023-12-31 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_alter_message_room_alter_message_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]