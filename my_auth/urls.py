from django.conf.urls import url
from my_auth import views as myviews

app_name = 'auth'
urlpatterns = [
    url(r'^login/$', myviews.MyLoginView.as_view(), name='login'),
    url(r'^logout/$', myviews.MyLogoutView.as_view(), name='logout'),

    url(r'^password_change/$', myviews.MyPasswordChangeView.as_view(), name='password_change'),
    url(r'^password_change/done/$', myviews.MyPasswordChangeDoneView.as_view(), name='password_change_done'),

    url(r'^password_reset/$', myviews.MyPasswordResetView.as_view(), name='password_reset'),
    url(r'^password_reset/done/$', myviews.MyPasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        myviews.MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset/done/$', myviews.MyPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]