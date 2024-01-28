from django.contrib import admin
#from base.models import Consumer
from base.models import Chat, Category, Message, Vote, VoteGroup, Profile

admin.site.register(Chat)
admin.site.register(Category)
admin.site.register(Message)
admin.site.register(Vote)
admin.site.register(VoteGroup)
admin.site.register(Profile)