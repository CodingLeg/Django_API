from django.contrib import admin
from .models import User, Group, Message, Member

admin.site.register(User)
admin.site.register(Message)
admin.site.register(Group)
admin.site.register(Member)



