from django.test import TestCase
from main.models import User, Group, Member, Message

class userTestCase(TestCase):
    def test_save_user(self):
        User.objects.create(
            username='savya', full_name='Savya Sachi', email='savya@gmail.com', password='00000'
        )
    
class groupTestCase(TestCase):
    def test_save_group(self):
        Group.objects.create(
            gpName='Swift', subscribe='Available', role='member'
        )

