from django.db import models
from django.utils.translation import gettext as _

from apps.product.models import ProductModel
from apps.user.models import User
from apps.utils.models import BaseModel


# Create your models here.
class Order(BaseModel):
    """
    Order model class
    """

    class OrderStatus(models.TextChoices):
        pending = 'pending', _("Pending")
        customer_confirmed = 'customer_confirmed', _("Customer Confirmed")
        admin_confirmed = 'admin_confirmed', _("Admin Confirmed")
        in_transit = 'in_transit', _("In-Transit")
        delivered = 'delivered', _("Delivered")
        in_return = 'return', _("Return")
        cancel = 'cancel', _("Cancel")

    customer = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        blank=True,
        related_name="customer_orders",
        verbose_name=_("Customer")
    )

    complete = models.BooleanField(
        default=False,
        verbose_name=_("Completed?")
    )

    coupon_code = models.CharField(
        default="None",
        max_length=200,
        blank=True,
        null=True,
        verbose_name=_("Coupon Code")
    )

    coupon_amount = models.FloatField(
        default=0,
        blank=True,
        null=True,
        verbose_name=_("Coupon Amount")
    )

    transaction_id = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name=_("Transaction Id")
    )

    method = models.CharField(
        max_length=200,
        null=True,
        verbose_name=_("Method")
    )

    delivery_fee = models.FloatField(
        default=0,
        blank=True,
        null=True,
        verbose_name=_("Delivery Fee")
    )

    total = models.FloatField(
        default=0,
        blank=True,
        null=True,
        verbose_name=_("Total")
    )

    advance = models.FloatField(
        default=0,
        blank=True,
        null=True,
        verbose_name=_("Advance")
    )

    due = models.FloatField(
        default=0,
        blank=True,
        null=True,
        verbose_name=_("Due")
    )

    status = models.CharField(
        default=OrderStatus.pending,
        max_length=200,
        blank=True,
        null=True,
        choices=OrderStatus.choices,
        verbose_name=_("Status")
    )

    address = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name=_("Address")
    )

    city = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name=_("City")
    )

    notes = models.TextField(
        verbose_name=_("Notes"),
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        # Calculate due based on total and advance
        self.due = max(0, self.total - self.advance)
        super(Order, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.uuid)[-5:]

    @property
    def shipping(self):
        shipping = False
        orderitems = self.order_products.all()
        for i in orderitems:
            if not i.product.digital:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.order_products.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.order_products.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(BaseModel):
    """
    Order item model class
    """
    product = models.ForeignKey(
        ProductModel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_("Order Product"),
        related_name=_("order_products")
    )

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name=_("order_products"),
        verbose_name=_("Order"),
    )

    quantity = models.IntegerField(
        default=0,
        null=True,
        blank=True,
        verbose_name=_("Quantity")
    )

    price = models.FloatField(
        default=0,
        blank=True,
        null=True,
        verbose_name=_("Price")
    )

    total = models.FloatField(
        default=0,
        blank=True,
        null=True,
        verbose_name=_("Total")
    )

    color = models.CharField(
        blank=True,
        null=True,
        max_length=100,
        verbose_name=_("Color")
    )

    size = models.CharField(
        blank=True,
        null=True,
        max_length=100,
        verbose_name=_("Size")
    )

    def __str__(self):
        return str(self.uuid)[:5]

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")
        ordering = ('-created_at',)


class Wishlist(BaseModel):
    """
    Wishlist model class
    """
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="customer_wishlist",
    )

    products = models.ManyToManyField(
        ProductModel,
        related_name="customer_wishlist"
    )
   