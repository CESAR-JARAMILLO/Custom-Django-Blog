from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Entry(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
