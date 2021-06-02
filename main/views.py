from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, MessageSerializer, GroupSerializer, MemberSerializer
from .models import User, Message, Group, Member


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        user = User.objects.all().order_by('id')
        return user


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer

    def get_queryset(self):
        message = Message.objects.all().order_by('id')
        return message


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer

    def get_queryset(self):
        group = Group.objects.all().order_by('id')
        return group


class MemberViewSet(viewsets.ModelViewSet):
    serializer_class = MemberSerializer

    def get_queryset(self):
        member = Member.objects.all().order_by('id')
        return member


class EventViewSet(viewsets.ModelViewSet):
    #  serializer_class = GroupSerializer

    def get_queryset(self):
        event = Group.objects.earliest('id')
        return event
