from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext as _

from apps.utils.models import BaseModel


# Create your models here.
class DeliveryChargeModel(BaseModel):
    """
    Delivery Charge model class
    """
    inside_fee = models.FloatField(
        default=0,
        verbose_name=_('Inside City Fee'),
    )

    outside_fee = models.FloatField(
        default=0,
        verbose_name=_('Outside City Fee')
    )

    discount = models.IntegerField(
        default=0,
        verbose_name=_('Discount')
    )

    def __str__(self):
        return "Delivery Charge"

    def save(self, *args, **kwargs):
        existing_instance = DeliveryChargeModel.objects.first()

        if existing_instance and self.pk != existing_instance.pk:
            # If there is an existing instance, and the current instance is not the same, raise an error
            raise ValidationError("There can be only one instance of DeliveryCharge.")

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Delivery Charge")
        verbose_name_plural = _("Delivery Charge")
        ordering = ("-created_at",)


class CouponModel(BaseModel):
    """
    Coupon model class
    """
    coupon_code = models.CharField(
        verbose_name=_("Coupon Code"),
        blank=True,
        null=True,
        max_length=100
    )

    amount = models.FloatField(
        default=0,
        verbose_name=_("Amount")
    )

    use_count = models.PositiveSmallIntegerField(
        default=0,
        verbose_name=_("Use Count"),
    )

    expire_date = models.DateTimeField(
        verbose_name=_("Expire Date"),
        blank=True,
        null=True
    )

    def __str__(self):
        return self.coupon_code

    class Meta:
        verbose_name = _("Coupon Code")
        verbose_name_plural = _("Coupon Codes")
        ordering = ("-created_at",)


class CampaignModel(BaseModel):
    """
    Campaign model class.
    """
    image = models.ImageField(
        verbose_name=_("Image"),
        upload_to="campaign/images"
    )

    title = models.CharField(
        max_length=50,
        verbose_name=_("Title"),
    )

    starts_with = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name=_("Starts with")
    )

    url_path = models.CharField(
        verbose_name=_("URL path"),
        blank=True,
        null=True,
        max_length=255,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Campaign")
        verbose_name_plural = _("Campaign")
        ordering = ("-created_at",)


class SubscriptionModel(BaseModel):
    """
    Subscription model class
    """

    email = models.EmailField(
        verbose_name=_("Email"),
        unique=True,
    )

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _("Subscriber")
        verbose_name_plural = _("Subscribers")
        ordering = ("-created_at",)
