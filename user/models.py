from django.db import models
from django.contrib.auth.base_user import BaseUserManager

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, email, password,user_type, is_staff=False, is_superuser=False, is_active=True,**extra_fields):
        email =UserManager.normalize_email(email)
        user =self.model(email=email,user_type=user_type, is_staff=is_staff, is_superuser=is_superuser, is_active=is_active,
        **extra_fields)

        if password:
            user.set_password(password)
            user.save()
            return user

    def create_user(self, email, password, is_staff=False, is_superuser=True, is_active=True, **extra_fields):
        email = UserManager.normalize_email(email)
        user = self.model(email=email, is_staff=is_staff, is_superuser=is_superuser, is_active=is_active,
                          **extra_fields)
        if password:
            user.set_password(password)
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, blank=False, null=False, unique=True)
    full_name = models.CharField(max_length=200, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now, editable=False)
    USER_TYPE_CHOICES = (
        (1, 'superadmin'),
        (2, 'administrator'),
        (3, 'editor'),
        (4, 'contributor'),
        (5, 'subscriber'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)

    USERNAME_FIELD = "email"
    objects = UserManager()

    def __str__(self):
        return f"{self.email} - {self.full_name}"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering =["-date_joined"]
        get_latest_by = "date-joined"