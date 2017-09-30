

def my_paginator_style(paginator, page, context, pages_num_2b_shown):
    '''
        this function calculate the page numbers to be shown in the home page and
        add this page numbers to the given context.
    '''
    context['multiple_page_series_to_show'] = 0
    if paginator.num_pages > pages_num_2b_shown:
        context['multiple_page_series_to_show'] = 1
        context['page_number_to_be_show'] = [i + page.number - pages_num_2b_shown // 2
                                             for i in range(pages_num_2b_shown)]
        if page.number < pages_num_2b_shown // 2:
            context['page_number_to_be_show'] = [i + 1 for i in
                                                 range(pages_num_2b_shown)]
        if page.number + pages_num_2b_shown // 2 >= paginator.num_pages:
            context['page_number_to_be_show'] = [i + paginator.num_pages - pages_num_2b_shown + 1
                                                 for i in range(pages_num_2b_shown)]
    return context