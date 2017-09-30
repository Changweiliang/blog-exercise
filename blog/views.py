from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from django.contrib.auth import decorators as auth_decorators
from django.views.generic import ListView
from . import models
from .forms.blog_form import BlogForm
from django.template.context import RequestContext
from my_auth.models import Permission
from .utils import my_paginator_style


class HomePage(ListView):
    model = models.MyPost
    template_name = 'blog/homepage.html'
    paginate_by = 4
    context_object_name = 'blog_list'

    def get_queryset(self):
        return models.MyPost.objects.all().order_by('-published_time')

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        queryset = self.get_queryset()
        paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, self.get_paginate_by(queryset))
        # add the page numbers to be shown in homepage to context
        context = my_paginator_style(paginator, page, context, pages_num_2b_shown=5)
        return context


def blog_detail(request, pk):
    blog = get_object_or_404(models.MyPost, pk=pk)
    template_name = 'blog/blog_detail.html'
    context = {
        'blog': blog
    }
    return render(request, template_name, context)


@auth_decorators.login_required
# @auth_decorators.permission_required(['blogs.edit_blog'], raise_exception=True)
def edit_blog(request,pk):
    blog_instance = get_object_or_404(models.MyPost, pk=pk)
    template_name = 'blog/edit_blog'
    context = {}
    if request.method == "POST":
        blog_edit_form = BlogForm(request.POST)
        if blog_edit_form.is_valid():
            blog_clean_data = blog_edit_form.cleaned_data
    else:
        blog_edit_form = BlogForm

    render(request, template_name, context)


@auth_decorators.login_required()
def create_blog(request):
    template_name = 'blog/create_blog.html'
    context = {}
    if request.method == 'POST':
        # print('if')
        new_blog_form = BlogForm(request.POST)
        # print(new_blog_form.is_valid())
        if new_blog_form.is_valid():
            new_blog_cd = new_blog_form.cleaned_data
            # print(request.user)
            new_blog = models.MyPost.objects.create(author=request.user,
                title=new_blog_cd['title'], tags=new_blog_cd['tags'],
                content=new_blog_cd['content'],published_time=new_blog_cd['published_time'],
                created_time=new_blog_cd['created_time']
            )
            #print(new_blog)
            new_blog.save()
            return HttpResponseRedirect(reverse('blog:blog_detail', args=(new_blog.id,)))
    else:
        #print('else')
        new_blog_form = BlogForm()
        context['blog_form'] = new_blog_form
        return render(request,template_name, context)