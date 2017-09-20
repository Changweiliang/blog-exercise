from django.shortcuts import render
from django.views.generic import ListView
from . import models


class HomePage(ListView):
    model = models.MyPost
    template_name = 'blog/homepage.html'
    paginate_by = 10