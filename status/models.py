from django.db import models
from django.contrib.auth.models import User


class Status(models.Model):
    text = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
