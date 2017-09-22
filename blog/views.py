from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from . import models
from django.core.paginator import Paginator


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

    context = {
        'blog': blog
    }
    return render(request, 'blog/blog_detail.html', context)