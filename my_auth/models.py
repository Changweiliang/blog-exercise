from django.contrib.auth import models as auth_models
from django.db import models
from django.utils.translation import ugettext_lazy as _


class PermissionManager(auth_models.PermissionManager):
    pass


class Permission(auth_models.Permission):
    pass


class GroupManager(auth_models.GroupManager):
    pass


class Group(auth_models.Group):
    pass


class UserManager(auth_models.UserManager):
    pass


class User(auth_models.AbstractUser):
    email = models.EmailField(_('email address'), unique=True)


class AnonymousUser(auth_models.AnonymousUser):
    pass