from django.contrib.auth import views


class MyLoginView(views.LoginView):
    template_name = 'registration/my_login.html'


class MyLogoutView(views.LogoutView):
    template_name = 'registration/my_logged_out.html'



class MyPasswordChangeView(views.PasswordChangeView):
    pass


class MyPasswordChangeDoneView(views.PasswordChangeDoneView):
    pass


class MyPasswordResetView(views.PasswordResetView):
    pass


class MyPasswordResetDoneView(views.PasswordResetDoneView):
    pass


class MyPasswordResetCompleteView(views.PasswordResetCompleteView):
    pass


class MyPasswordResetConfirmView(views.PasswordResetConfirmView):
    pass