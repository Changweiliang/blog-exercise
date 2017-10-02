from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from django.contrib.auth import decorators as auth_decorators
from django.views.generic import ListView
from . import models
from .forms.blog_form import BlogForm
from django.template.context import RequestContext
from my_auth.models import Permission


class HomePage(ListView):
    model = models.MyPost
    template_name = 'blog/homepage.html'
    paginate_by = 4
    context_object_name = 'blog_list'

    def get_queryset(self):
        return models.MyPost.objects.all().order_by('-published_time')

    def get_context_data(self, **kwargs):
        pages_to_show_in_one_series = 5
        context = super(ListView, self).get_context_data(**kwargs)
        queryset = self.get_queryset()
        page_size = self.get_paginate_by(queryset)
        paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, page_size)
        # if there are multiple_page_series_to_show,
        # the way to show page is different in template
        # otherwise the page list is simple
        context['multiple_page_series_to_show'] = 0

        if paginator.num_pages > pages_to_show_in_one_series:
            context['multiple_page_series_to_show'] = 1
            context['page_number_to_be_show'] = [i + page.number - pages_to_show_in_one_series // 2
                                                 for i in range(pages_to_show_in_one_series)]
            if page.number < pages_to_show_in_one_series//2:
                context['page_number_to_be_show'] = [i+1 for i in
                                                     range(pages_to_show_in_one_series)]
            if page.number + pages_to_show_in_one_series//2 >= paginator.num_pages:
                context['page_number_to_be_show'] = [i+paginator.num_pages-pages_to_show_in_one_series+1
                                                     for i in range(pages_to_show_in_one_series)]
        return context


def blog_detail(request, pk):
    blog = get_object_or_404(models.MyPost, pk=pk)
    template_name = 'blog/blog_detail.html'
    context = {
        'blog': blog
    }

    return render(request, template_name, context)


@auth_decorators.login_required
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
        print('if')
        new_blog_form = BlogForm(request.POST)
        print(new_blog_form.is_valid())
        if new_blog_form.is_valid():
            new_blog_cd = new_blog_form.cleaned_data
            new_blog = models.MyPost.objects.create(author=request.user, **new_blog_cd)
            new_blog.save()
            return HttpResponseRedirect(reverse('blog:blog_detail', args=(new_blog.id,)))
    else:
        print('else')
        new_blog_form = BlogForm()
        context['blog_form'] = new_blog_form
        return render(request,template_name, context)