from django.shortcuts import render, get_object_or_404
from django.contrib.auth import decorators as auth_decorators
from django.views.generic import ListView
from . import models
from .forms.blog_form import BlogForm
from django.template.context import RequestContext


class HomePage(ListView):
    model = models.MyPost
    template_name = 'blog/homepage.html'
    paginate_by = 4
    context_object_name = 'blog_list'

    def get_queryset(self):
        return models.MyPost.objects.all().order_by('published_time')

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
@auth_decorators.permission_required(['blogs.edit_blog'], raise_exception=True)
def edit_blog(request,pk):
    blog = get_object_or_404(models.MyPost, pk=pk)
    template_name = 'blog/edit_blog'
    if request.method == "POST":
        pass
    else:
        blog_edit_form = BlogForm

    context = RequestContext(request)

    render(request, template_name, context)

