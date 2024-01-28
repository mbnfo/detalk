from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from django.db.models import Q
from base.models import Chat, Message, Vote, VoteGroup, Profile, Category
from base.serializers import UserSerializer, ChatSerializer, MessageSerializer, VoteSerializer, VoteGroupSerializer, ProfileSerializer, CategorySerializer
from django.db.models import F, Func

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        return token
        

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def createUser(request):
    new_user = User.objects.create_user(username = request.data['username'], password = request.data['password'], email = request.data['email'])
    prof = Profile.objects.create(user = new_user, username = new_user.username)
    return Response('this model has been created')


#also add a maintainance page

@api_view(['POST'])
def anonUser (request):
    user_count = User.objects.all().count()
    pword = 'anonouser'
    new_user = User.objects.create_user(username = 'Unknown_user' + str(user_count), password = 'anonouser' , email = 'anon@usesr.number' + str(user_count))
    prof = Profile.objects.create(user = new_user, username = new_user.username)
    user_serializer = UserSerializer(new_user, many = False)

    return Response (user_serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def settings(request):
    user_info = request.user
    prof = Profile.objects.get(user = user_info)
    prof.bio = request.data['bio']
    prof.link = request.data['link']
    prof.save()

    cat1 = Category.objects.get(name = request.data['category_1'])
    cat2 = Category.objects.get(name = request.data['category_2'])
    cat3 = Category.objects.get(name = request.data['category_3'])

    cat1.users.add(prof)
    cat2.users.add(prof)
    cat3.users.add(prof)

    return Response('Bio and category successfully created!')
#get user information

@api_view(['GET'])
def userInfo(request):
    user = request.user
    user_serializer = UserSerializer(user, many = False)
    return Response (user_serializer.data)

@api_view(['GET'])
def getProfile(request, pk):
    user_obj = User.objects.get(id = pk) 
    prof = Profile.objects.get(user = user_obj)
    prof_serializer = ProfileSerializer(prof, many = False)
    return Response (prof_serializer.data)    

#checks/ removals / addition of followers
@api_view(['GET'])
def checkFollowing(request, pk):
    query_profile = Profile.objects.get(id = pk)
    user = request.user


    if user in query_profile.followers.all():
        return Response(True)
    else:
        return Response(False)
    return Response('an error occured')

@api_view(['POST'])
def changeFollowing(request, pk):
    query_profile = Profile.objects.get(id = pk)
    user = request.user


    if user in query_profile.followers.all():
        query_profile.followers.remove(user)
        return Response(False)
    else:
        query_profile.followers.add(user)
        return Response(True)
    return Response('an error occured')


#returns the chatrooms to the api front end     
@api_view(['GET'])
def chatroom_api(request):
    user = request.user
    prof = Profile.objects.get(user = user)
    chat = prof.chat_set.all()
    chat_serializer = ChatSerializer(chat, many = True)
    return Response (chat_serializer.data)

@api_view(['POST'])
def exit_group(request, pk):
    prof = Profile.objects.get(user = request.user)
    room = Chat.objects.get(id = pk)

    room.participants.remove(prof)

    return Response('successfully exited group')


#this is the chatroom messages request section

@api_view(['GET'])
def room(request, pk):
    prof = Profile.objects.get(user = request.user)

    chatroom = Chat.objects.get(id = int(pk))
    if prof in chatroom.participants.all():
        chatroom_serializer = ChatSerializer(chatroom, many = False)

        return Response (chatroom_serializer.data)

    else:
        return Response('this user is not a part of this chatroom')
    return Response ('an error occured!')


#message section

@api_view(['GET'])
def messages(request, pk):
    chatroom = Chat.objects.get(id = int(pk))
    message = chatroom.message_set.all()
    message_serializer = MessageSerializer(message, many = True)
    return Response(message_serializer.data)

@api_view(['POST'])
def create_message(request):
    chatroom = Chat.objects.get(id = int(request.data['room_id']))
    new_message = Message.objects.create(value = request.data['message'], room = chatroom, user = request.user.username)
    new_message.save()
    return Response('message succesfully created!')


@api_view(['POST'])
def like_message(request, pk):
    message = Message.objects.get(id = pk)
    prof = Profile.objects.get(user = request.user)
    if prof in message.liked_by.all():
        Message.objects.filter(id = pk).update(likes = F('likes') - 1)
        message.liked_by.remove(prof)
    else:
        Message.objects.filter(id = pk).update(likes = F('likes') + 1)
        message.liked_by.add(prof)
    return Response('message like counter has been altered')


        

#chatroom votes section

@api_view(['POST'])
def create_votes(request):
    vote1 = Vote.objects.create(name = request.data['vote1'])
    vote2 = Vote.objects.create(name = request.data['vote2'])

    vote_group = VoteGroup.objects.create()
    vote_group.votes.add(vote1, vote2)
    vote_group_serializer = VoteGroupSerializer(vote_group)

    return Response (vote_group_serializer.data)

@api_view(['GET'])
def get_vote(request, pk):
    chat = Chat.objects.get(id = pk)
    votegroup = VoteGroup.objects.get(room = chat)
    votes = votegroup.votes.all()
    vote_serializer = VoteSerializer(votes, many = True)

    return Response(vote_serializer.data)


@api_view(['GET'])
def get_vote_group(request, pk):
    chatroom = Chat.objects.get(id = pk)
    vote_group = VoteGroup.objects.get(room = chatroom)

    vote_group_serializer = VoteGroupSerializer(vote_group, many = False)

    return Response (vote_group_serializer.data)


@api_view(['POST'])
def voted (request, pk):
    voted = Vote.objects.get(name = pk)
    vote_group = VoteGroup.objects.get(votes = voted.id)
    prof = Profile.objects.get(user = request.user)

    if prof in vote_group.voted_users.all():
        return Response('cant vote anymore')
    else:

        VoteGroup.objects.filter(id=vote_group.id).update(total=F('total') + 1)
        Vote.objects.filter(name = voted.name).update(assigned = F('assigned') + 1)
        vote_group.voted_users.add(prof)

        return Response('vote succesfully')

#this is the chatroom creation section
@api_view(['POST'])
def create_room(request):
    prof = Profile.objects.get(user = request.user)

    category = Category.objects.get(name = request.data['category'])

    new_chat_room = Chat.objects.create(name = request.data['name'], description = request.data['description'], cat = category)
    all_users =  Profile.objects.all()#in official release allow all the partiipant picking event to be done by this filter ------------>     #category.users.all().order_by('?').values_list('id', flat = True)[:15]
    new_chat_room.participants.set(all_users)
    new_chat_room.participants.add(prof)
    Profile.objects.filter(user=request.user).update(chat_count=F('chat_count') + 1)
    if request.data['vote_id'] == 0:
        pass
    else:
        vote_group = VoteGroup.objects.get(id = request.data['vote_id'])
        vote_group.room = new_chat_room
        vote_group.save()
        new_chat_room.includesVotes = True
        new_chat_room.save()

    return Response ('chat room created')



@api_view(['GET'])
def get_categories(request):
    category = Category.objects.all()
    category_serializer = CategorySerializer(category, many = True)
    return Response(category_serializer.data)

