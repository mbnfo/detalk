from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from base.models import Chat, Message, Vote, Profile, VoteGroup, Category


'''
class BidSerializer(ModelSerializer):
    class Meta:
        model = Bids
        fields = '__all__'
'''

class UserSerializer (ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id', 'password')

class ChatSerializer (ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'

class MessageSerializer (ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class VoteSerializer (ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'
class VoteGroupSerializer (ModelSerializer):
    class Meta:
        model = VoteGroup
        fields = '__all__'

class ProfileSerializer (ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class CategorySerializer (ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'