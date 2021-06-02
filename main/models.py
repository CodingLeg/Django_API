import datetime

from django.db import models
from django.db.models import CASCADE


class User(models.Model):
    username = models.CharField(max_length=100, unique=True, )
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class Group(models.Model):
    gpName = models.CharField(max_length=100, unique=True, default='Java')
    subscribe = models.CharField(max_length=100, default='okay')
    role = models.CharField(max_length=100, default='user')

    def __str__(self):
        return self.gpName


class Member(models.Model):
    grp_ID = models.ForeignKey(Group, on_delete=CASCADE)
    user_ID = models.ForeignKey(User, on_delete=CASCADE)
    role = models.CharField(max_length=100, default="user")
    gpName = models.CharField(max_length=100, default="Java")


class Message(models.Model):
    grp_ID = models.ForeignKey(Group, on_delete=CASCADE)
    user = models.CharField(max_length=100, default='manager')
    group = models.CharField(max_length=100, default='Java')
    messages = models.CharField(max_length=100, default='Welcome')

    def __str__(self):
        return self.group
