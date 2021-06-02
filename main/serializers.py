from rest_framework import serializers
from .models import User, Message, Group, Member


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'full_name', 'email', 'password')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'gpName', 'subscribe', 'role', )


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'grp_ID', 'user', 'group', 'messages')


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'grp_ID', 'user_ID', 'role', 'gpName')
        #depth = 2
