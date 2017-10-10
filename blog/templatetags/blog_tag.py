from django import template
from django.utils.html import format_html

register = template.Library()

@register.simple_tag
def real_name_or_username(blog):
    if blog.author.first_name and blog.author.last_name:
        return format_html('%s' % blog.author.first_name), format_html(blog.author.last_name)
    else:
        return blog.author.username


@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})