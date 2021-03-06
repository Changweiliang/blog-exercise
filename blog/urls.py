from django.conf.urls import url
from . import views


app_name = 'blog'
urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='homepage'),
    url(r'^(?P<pk>\d+)/detail/$', views.blog_detail, name='blog_detail'),
    url(r'^(?P<pk>\d+)/edit/$', views.edit_blog, name='edit_blog'),
    url(r'^create/$', views.create_blog, name='create_blog'),
    url(r'^draft/$', views.DraftBlog.as_view(), name='draft_blog'),
    url(r'^private/$', views.PrivateBlog.as_view(), name='private_blog'),
    url(r'^myblog/$', views.MyBlog.as_view(), name='my_blog'),
    url(r'^blogger/$', views.UserList.as_view(), name='blogger'),
]
