from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from django.contrib.auth import decorators as auth_decorators
from django.views.generic import ListView
from . import models
from .forms.blog_form import BlogForm
from my_auth.models import User
from .utils import my_paginator_style
from django.contrib.auth.mixins import LoginRequiredMixin


class MyPaginatedBlogListView(ListView):
    model = models.MyPost
    paginate_by = 5
    context_object_name = 'blog_list'

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        queryset = self.get_queryset()
        paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, self.get_paginate_by(queryset))
        # add the page numbers to be shown in homepage to context
        context = my_paginator_style(paginator, page, context, pages_num_2b_shown=5)
        return context


class UserList(MyPaginatedBlogListView):
    model = User
    template_name = 'blog/blogger_list.html'
    context_object_name = 'blogger_list'

    def get_queryset(self):
        return User.objects.all().order_by('username')


class HomePage(MyPaginatedBlogListView):
    model = models.MyPost
    template_name = 'blog/homepage.html'
    paginate_by = 5
    context_object_name = 'blog_list'

    def get_queryset(self):
        return models.MyPost.objects.filter(is_draft=False, is_private=False).order_by('-published_time')


class MyBlog(LoginRequiredMixin, MyPaginatedBlogListView):
    model = models.MyPost
    login_url = 'auth:login'
    template_name = 'blog/my_blog_list.html'
    paginate_by = 5
    context_object_name = 'blog_list'

    def get_queryset(self):
        return models.MyPost.objects.filter(author__username=self.request.user.username,
                                              is_draft=False, is_private=False).order_by('-published_time')


class DraftBlog(LoginRequiredMixin, MyPaginatedBlogListView):
    model = models.MyPost
    login_url = 'auth:login'
    template_name = 'blog/draft_list.html'
    paginate_by = 5
    context_object_name = 'blog_list'

    def get_queryset(self):
        return models.MyPost.objects.filter(author__username=self.request.user.username,
                                              is_draft=True, is_private=False).order_by('-published_time')


class PrivateBlog(LoginRequiredMixin, MyPaginatedBlogListView):
    model = models.MyPost
    login_url = 'auth:login'
    template_name = 'blog/private_list.html'
    paginate_by = 5
    context_object_name = 'blog_list'

    def get_queryset(self):
        return models.MyPost.objects.filter(author__username=self.request.user.username,
                                                is_draft=False, is_private=True).order_by('-published_time')


def blog_detail(request, pk):
    blog_instance = get_object_or_404(models.MyPost, pk=pk)

    # need to add permission to protect draft blog and private blog

    template_name = 'blog/blog_detail.html'
    if blog_instance.author.username == request.user.username or request.user.is_superuser:
        blog_instance.can_be_edited = True
    context = {
        'blog': blog_instance,
    }
    return render(request, template_name, context)


@auth_decorators.login_required(login_url = 'auth:login')
def edit_blog(request,pk):
    blog_instance = get_object_or_404(models.MyPost, pk=pk)
    template_name = 'blog/edit_blog.html'
    context = {}
    # if request user is the owner of the blog
    if blog_instance.author.username == request.user.username or request.user.is_superuser:
        if request.method == "POST":
            blog_edit_form = BlogForm(request.POST)
            if blog_edit_form.is_valid():
                blog_cd = blog_edit_form.cleaned_data
                blog_instance.title, blog_instance.tags, blog_instance.content, blog_instance.published_time, blog_instance.created_time \
                    = blog_cd['title'], blog_cd['tags'], blog_cd['content'], blog_cd['published_time'], blog_cd['created_time']
                print('save_as_draft' in request.POST, 'publish' in request.POST)
                if 'save_as_draft' in request.POST:
                    blog_instance.is_draft = True
                elif 'publish' in request.POST:
                    blog_instance.is_draft = False
                blog_instance.save()
                return HttpResponseRedirect(reverse('blog:blog_detail', args=(blog_instance.id,)))
        else:
            blog_edit_form = BlogForm(initial={
                'title': blog_instance.title,
                'tags': blog_instance.tags,
                'content': blog_instance.content,
                'published_time': blog_instance.published_time,
                'created_time': blog_instance.created_time,
            })
            context['blog_edit_form'] = blog_edit_form
            return render(request, template_name, context)
    else:
        context['permission_error'] = True
        template_name = 'registration/permission_denied.html'
        return render(request, template_name, context)


@auth_decorators.login_required(login_url = 'auth:login')
def create_blog(request):
    template_name = 'blog/create_blog.html'
    context = {}
    if request.method == 'POST':
        # print('if')
        new_blog_form = BlogForm(request.POST)
        # print(new_blog_form.is_valid())
        if new_blog_form.is_valid():
            new_blog_cd = new_blog_form.cleaned_data
            new_blog = models.MyPost.objects.create(author=request.user, **new_blog_cd)
            # print(request.user)
            new_blog = models.MyPost.objects.create(author=request.user,**new_blog_cd)
            if 'save_as_draft' in request.POST:
                new_blog.is_draft = True
            elif 'Publish' in request.POST:
                new_blog.is_draft = False
            #print(new_blog.is_draft)
            new_blog.save()
            return HttpResponseRedirect(reverse('blog:blog_detail', args=(new_blog.id,)))
    else:
        #print('else')
        new_blog_form = BlogForm()
        context['blog_form'] = new_blog_form
        return render(request,template_name, context)
