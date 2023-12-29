import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


USER = get_user_model()


class BaseModel(models.Model):
    """
    Base model for other models
    """
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        primary_key=True,
        verbose_name=_('uuid')
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created at?')
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Updated at?')
    )

    created_by = models.ForeignKey(
        to=USER,
        verbose_name=_('Created by'),
        null=True,
        blank=True,
        related_name='%(class)s_created',
        on_delete=models.PROTECT
    )

    updated_by = models.ForeignKey(
        to=USER,
        verbose_name=_('Updated by'),
        null=True,
        blank=True,
        related_name='%(class)s_updated',
        on_delete=models.PROTECT
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Is active?')
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        Override the save method to set created_by and updated_by fields.
        """
        user = kwargs.pop('user', None)  # Get the user from kwargs
        update_fields = kwargs.get('update_fields', None)

        # Set created_by and updated_by only on creation (not when updating)
        if not self.pk:
            self.created_by = user

        if update_fields and 'updated_by' in update_fields:
            self.updated_by = user

        super(BaseModel, self).save(*args, **kwargs)

    @classmethod
    def get_all_default_model_fields_name(cls):
        """
        Return list of all fields of this model
        """
        field_name = []
        for field in cls._meta.fields:
            field_name.append(field.name)
        return field_name

    @classmethod
    def active(cls):
        """
        Get list of active objects
        @return: Filtered queryset
        """
        return cls.objects.filter(is_active=True)

    @classmethod
    def inactive(cls):
        """
        Get list of inactive objects
        @return: Filtered queryset
        """
        return cls.objects.filter(is_active=False)