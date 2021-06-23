from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Posts(models.Model):
    post = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    liked_users = models.ManyToManyField(User, blank=True, related_name="liked_posts")
    time = models.DateTimeField( auto_now_add=True)
    
class follow_db(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="User")
    followers = models.ManyToManyField(User, blank=True, related_name="following")
