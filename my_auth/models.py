from django.contrib.auth import models


class PermissionManager(models.PermissionManager):
    pass


class Permission(models.Permission):
    pass


class GroupManager(models.GroupManager):
    pass


class Group(models.Group):
    pass


class UserManager(models.UserManager):
    pass


class User(models.AbstractUser):
    pass


class AnonymousUser(models.AnonymousUser):
    pass