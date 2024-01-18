from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from phonenumber_field import modelfields

from .managers import UserManager
from organizations.models import Organization


class User(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(
        unique=True,
        verbose_name='Email address',
    )
    phone_number = modelfields.PhoneNumberField(
        blank=True,
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.SET_NULL,
        null=True,
        related_name="users",
    )
    is_admin = models.BooleanField(
        verbose_name=('Is admin'),
        default=False,
    )
    created_at = models.DateTimeField(
        verbose_name=('Created at'),
        auto_now_add=True,
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm: str, obj=None) -> bool:
        return True

    def has_module_perms(self, app_label: str) -> bool:
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        ordering = ['created_at', ]
        verbose_name = 'User'
        verbose_name_plural = 'Users'