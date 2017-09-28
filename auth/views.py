from django.contrib.auth import views


class MyLoginView(views.LoginView):
    pass


class MyLogoutView(views.LogoutView):
    pass