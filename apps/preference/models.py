from django.db import models
from django.utils.translation import gettext as _
from apps.utils.models import BaseModel


# Create your models here.
class MenuModel(BaseModel):
    """
    Menu model Class.
    """
    name = models.CharField(
        verbose_name=_("name"),
        max_length=100,
    )

    position = models.PositiveSmallIntegerField(
        verbose_name=_("Position"),
        default=0,
    )

    url_path = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_('URL path')
    )

    class MenuType(models.TextChoices):
        main = 'main', _("Main")
        footer1 = 'footer1', _("Footer 1")
        footer2 = 'footer2', _("Footer 2")

    type = models.CharField(
        max_length=255,
        choices=[(choice, choice) for choice in MenuType.values],
        default=MenuType.main,
        verbose_name=_('Type'),
    )

    def __str__(self):
        return self.name
