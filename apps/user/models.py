from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

from apps.user.managers import UserManager


class User(AbstractUser):
    name = models.CharField(verbose_name=_("Name"), max_length=100)
    phone = models.CharField(
        verbose_name=_("Phone"),
        unique=True,
        db_index=True,
        blank=True,
        null=True,
        max_length=15
    )
    email = models.EmailField(
        verbose_name=_("Email"),
        blank=True,
        null=True
    )
    avatar = models.ImageField(
        verbose_name=_("Avatar"), upload_to="avatar/", null=True, blank=True
    )
    ROLE_CHOICES = (
        ("customer", _("Customer")),
        ("staff", _("Staff")),
    )
    role = models.CharField(
        verbose_name=_("Role"),
        db_index=True,
        max_length=35,
        choices=ROLE_CHOICES,
        default="customer",
    )
    objects = UserManager()
    REQUIRED_FIELDS = ["name"]
    USERNAME_FIELD = 'phone'

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["name"]

    def __str__(self):
        return self.username
