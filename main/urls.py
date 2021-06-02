from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, MessageViewSet, GroupViewSet, MemberViewSet

router = routers.DefaultRouter()

router.register(r'user', UserViewSet, basename="user")
router.register(r'message', MessageViewSet, basename="message")
router.register(r'group', GroupViewSet, basename="group")
router.register(r'member', MemberViewSet, basename="member")
router.register(r'event', MemberViewSet, basename="event")


urlpatterns = [
    path('', include(router.urls))
]
