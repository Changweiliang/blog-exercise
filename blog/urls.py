from django.conf.urls import url
from . import views


app_name = 'blog'
urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='homepage'),
    url(r'^(?P<pk>\d+)/detail/$', views.blog_detail, name='blog_detail'),
    url(r'^(?P<pk>\d+)/edit/$', views.edit_blog, name='blog_edit')
]
