from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext as _

from apps.utils.models import BaseModel


# Create your models here.
class BlogModel(BaseModel):
    """
    Blog model class.
    """

    title = models.CharField(
        max_length=255,
        verbose_name=_("Title")
    )

    content = RichTextField(
        verbose_name=_("Content")
    )

    thumbnail = models.ImageField(
        verbose_name=_("Thumbnail"),
        upload_to="blog/images"
    )

    video = models.FileField(
        verbose_name=_("Video"),
        blank=True,
        null=True,
        upload_to="blog/videos"
    )

    view_count = models.IntegerField(
        default=0,
        verbose_name=_("View Count"),
        blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")
        ordering = ("-created_at",)


    def increment_views(self):
        """
        Increment the view count by 1.
        """
        self.view_count += 1
        self.save(update_fields=['view_count'])
