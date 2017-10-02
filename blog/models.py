from django.db import models
from django.utils import timezone
from django.conf import settings
from django.shortcuts import reverse

# default_user_id = 1 default=default_user_id,
# Create your models here.
class MyPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    tags = models.CharField(max_length=20, null=True, blank=True)
    published_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(default=timezone.now)
    is_draft = models.BooleanField(default=False)
    is_private = models.BooleanField(default=False)
    can_be_edited = models.BooleanField(default=False)
    allow_comment = models.BooleanField(default=True)

    class Meta:
        ordering = ['published_time']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog_detail', args=[str(self.id)])


class PostComment(models.Model):
    pass