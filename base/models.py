from django.db import models
from django.contrib.auth.models import User


class Profile (models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    username = models.CharField(max_length = 250, blank = True)
    followers = models.ManyToManyField(User, blank = True, related_name = 'followers')
    bio = models.CharField(max_length = 1250 ,blank = True)
    link = models.CharField(max_length = 250, default = 'this person doesnt have any links', blank = True, null = True)
    chat_count = models.IntegerField(default = 0)

class Category (models.Model):
    name = models.CharField(max_length = 250)
    users = models.ManyToManyField(Profile, blank = True)

class Chat (models.Model):
    name = models.CharField(max_length = 250, blank = True)
    description = models.TextField(max_length = 250)
    cat = models.ForeignKey(Category, null = True, blank = True, on_delete = models.CASCADE)
    participants = models.ManyToManyField(Profile, blank = True)
    includeVotes = models.BooleanField(default = False)

class Message (models.Model):
    value = models.TextField(max_length = 1250, blank = True)
    user = models.CharField(max_length = 250, null = True, blank = True)
    room = models.ForeignKey(Chat, on_delete = models.CASCADE, null = True, blank = True)
    likes = models.IntegerField(default = 0)
    liked_by = models.ManyToManyField(Profile, blank = True)

class Vote (models.Model):
    name = models.CharField(max_length = 250, blank = True)
    percentage = models.FloatField(default = 0)
    assigned = models.IntegerField(default = 0)

class VoteGroup (models.Model):
    votes = models.ManyToManyField(Vote, blank = True)
    voted_users = models.ManyToManyField(Profile, blank = True)
    total = models.IntegerField(default = 0)
    room = models.ForeignKey(Chat, blank = True, on_delete = models.CASCADE, null = True)
