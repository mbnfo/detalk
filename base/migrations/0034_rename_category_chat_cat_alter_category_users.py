# Generated by Django 4.2.6 on 2024-01-26 14:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0033_remove_category_users_category_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='category',
            new_name='cat',
        ),
        migrations.AlterField(
            model_name='category',
            name='users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
