from django import forms
from django.forms import ModelForm
from blog.models import MyPost

class BlogForm(ModelForm):
    class Meta:
        model = MyPost
        fields = ['title','tags','content','published_time','created_time']
        localized_fields = ('published_time','created_time')