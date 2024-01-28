from django.urls import path
from . import views
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path ('token/', MyTokenObtainPairView.as_view(), name = 'token_obtain_pair'),
    path ('token/refresh/', TokenRefreshView.as_view(),name = 'token_refresh'),

    path ('authentification/create/user/', views.createUser, name = 'createUser'),
    path ('authentification/create/anon/', views.anonUser, name = 'create an anonymous user'),
    path ('create/user/settings/', views.settings, name = 'settings'),

    path ('user/', views.userInfo, name = 'user information'),
    path ('user/profile/<int:pk>/', views.getProfile, name = 'user profile information'),

    path ('user/profile/following/status/<int:pk>/', views.checkFollowing, name = 'check if user is following profile'),
    path ('user/profile/following/change/<int:pk>/', views.changeFollowing, name = 'change following status'),
    
    path ('home/chatrooms/', views.chatroom_api, name = 'chatroom api'),
    path('home/room/messages/like/<int:pk>/', views.like_message, name = 'change the like counter of a message'),

    path ('home/room/request/<int:pk>/', views.room, name = 'chatroom_access'),
    path ('home/room/messages/<int:pk>/', views.messages, name = 'messages'),
    path ('home/room/messages/create/', views.create_message, name = 'create new message'),
    path ('home/room/exitgroup/<int:pk>/', views.exit_group, name = 'exit chat'),

    path ('home/room/get/group/<int:pk>/', views.get_vote_group, name = 'get the vote_group data'),
    path ('home/create/vote/', views.create_votes, name = 'create votes and add them to a vote group'),
    path ('home/room/votes/<int:pk>/', views.get_vote, name = 'get chatroom votes'),
    path ('home/room/vote/<str:pk>/', views.voted, name = 'vote'),

    path ('home/get/categories/', views.get_categories, name = 'get categories'),
    path ('home/create/', views.create_room, name = 'create chat room'),
]
