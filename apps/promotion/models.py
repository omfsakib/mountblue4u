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