from django.db import models
from django.contrib.auth.models import User


class Status(models.Model):
    text = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

class UserFollow(models.Model):
    from_user = models.ForeignKey(User, related_name="following")
    to_user = models.ForeignKey(User, related_name="follower")
    time = models.DateTimeField(auto_now_add=True)
