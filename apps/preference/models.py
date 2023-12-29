from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify
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

    class Meta:
        verbose_name = _("Menu")
        verbose_name_plural = _("Menus")
        ordering = ('-created_at',)


class PreferenceModel(BaseModel):
    """
    Preference model class.
    """

    logo = models.ImageField(
        verbose_name="logo",
        blank=True,
        null=True,
        upload_to="logo/"
    )

    site_name = models.CharField(
        verbose_name=_("Site Name"),
        blank=True,
        null=True,
        max_length=50,
    )

    address = models.TextField(
        verbose_name=_("Address"),
        blank=True,
        null=True
    )

    phone = models.CharField(
        max_length=20,
        verbose_name=_("Phone Number"),
        blank=True,
        null=True
    )

    email = models.EmailField(
        verbose_name=_("Email"),
        blank=True,
        null=True
    )

    footer_about = models.TextField(
        verbose_name=_("Footer About"),
        blank=True,
        null=True
    )

    facebook = models.URLField(
        verbose_name=_('Facebook'),
        null=True,
        blank=True
    )

    twitter = models.URLField(
        verbose_name=_('Twitter'),
        null=True,
        blank=True
    )

    linkedin = models.URLField(
        verbose_name=_('Linkedin'),
        null=True,
        blank=True
    )

    youtube = models.URLField(
        verbose_name=_('Youtube'),
        null=True,
        blank=True
    )

    whatsapp = models.URLField(
        verbose_name=_('WhatsApp'),
        null=True,
        blank=True
    )

    instagram = models.URLField(
        verbose_name=_('Instagram'),
        null=True,
        blank=True
    )

    poster_image = models.ImageField(
        verbose_name=_('Poster Image'),
        upload_to="poster/image/",
        null=True,
        blank=True
    )

    poster_url = models.URLField(
        verbose_name=_('Poster Url'),
        blank=True,
        null=True
    )

    def __str__(self):
        return self.site_name

    def save(self, *args, **kwargs):
        existing_instance = PreferenceModel.objects.first()

        if existing_instance and self.pk != existing_instance.pk:
            # If there is an existing instance, and the current instance is not the same, raise an error
            raise ValidationError("There can be only one instance of PreferenceModel.")

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Preference")
        verbose_name_plural = _("Preferences")
        ordering = ('-created_at',)



class PageModel(BaseModel):
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=250
    )

    slug = models.SlugField(
        verbose_name=_('Slug'),
        max_length=255,
        unique=True,
        blank=True,
        null=True
    )

    content = RichTextField(
        verbose_name=_('Content')
    )

    feature_image = models.ImageField(
        verbose_name=_('Feature Image'),
        blank=True,
        null=True,
        upload_to="feature/image"
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(PageModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = _("Page")
        verbose_name_plural = _("Pages")
        ordering = ('-created_at',)