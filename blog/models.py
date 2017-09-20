from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class MyPost(models.Model):
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=100)
    post_tags = models.CharField(max_length=20, null=True)
    published_time = models.DateTimeField()
    created_time = models.DateTimeField(default=timezone.now)