from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


default_author = 1
# Create your models here.
class MyPost(models.Model):
    author = models.ForeignKey(User, default=default_author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    tags = models.CharField(max_length=20, null=True, blank=True)
    published_time = models.DateTimeField()
    created_time = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['published_time']

    def __str__(self):
        return self.title