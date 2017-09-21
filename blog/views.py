from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from . import models


class HomePage(ListView):
    model = models.MyPost
    template_name = 'blog/homepage.html'
    paginate_by = 10
    context_object_name = 'blog_list'

    def get_queryset(self):
        return models.MyPost.objects.all().order_by('-published_time')



def blog_detail(request, pk):
    blog = get_object_or_404(models.MyPost, pk=pk)

    context = {
        'blog': blog
    }
    return render(request, 'blog/blog_detail.html', context)