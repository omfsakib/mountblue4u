from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import FileExtensionValidator

from colorfield.fields import ColorField
from ckeditor.fields import RichTextField

from apps.utils.models import BaseModel


# Create your models here.
class CategoryModel(BaseModel):
    """
    Category Model Class.
    """
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=255,
    )

    image = models.ImageField(
        verbose_name=_('Image'),
        blank=True,
        null=True
    )

    is_featured = models.BooleanField(
        verbose_name=_("Is featured?"),
        default=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ('-created_at',)


class SizeModel(BaseModel):
    """
    Size model class.
    """
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=25,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Size")
        verbose_name_plural = _("Sizes")
        ordering = ('-created_at',)


class ColorModel(BaseModel):
    """
    Color model class.
    """
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=255,
    )

    code = ColorField(
        max_length=7,
        verbose_name=_('Color Code'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Color")
        verbose_name_plural = _("Colors")
        ordering = ('-created_at',)


class ProductModel(BaseModel):
    """
    Product Model Class.
    """
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=255,
    )

    price = models.FloatField(
        verbose_name=_('Price'),
        default=0.0,
    )

    discount_amount = models.FloatField(
        verbose_name=_("Discount Amount"),
        default=0.0
    )

    description = RichTextField(
        verbose_name=_("Description"),
        blank=True,
        null=True
    )

    rating = models.FloatField(
        default=0.0,
        verbose_name=_("Rating")
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ('-created_at',)


class ProductVariantModel(BaseModel):
    """
    Product Variant model class.
    """
    product = models.ForeignKey(
        ProductModel,
        verbose_name=_("Product"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    size = models.ForeignKey(
        SizeModel,
        verbose_name=_("Size"),
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    color = models.ForeignKey(
        ColorModel,
        verbose_name=_("Color"),
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    stock = models.PositiveIntegerField(
        verbose_name=_('Stock Quantity'),
        default=0,
    )

    code = models.CharField(
        verbose_name=_("Product Code"),
        max_length=50,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = _("Product Variant")
        verbose_name_plural = _("Product Variants")
        ordering = ('-created_at',)


class ProductImagesModel(BaseModel):
    """
    Product images model class.
    """
    product = models.ForeignKey(
        ProductModel,
        verbose_name=_("Product"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    image = models.ImageField(
        verbose_name=_('Image'),
        upload_to="images/"
    )

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")
        ordering = ('-created_at',)


class ProductVideosModel(BaseModel):
    """
    Product video model class
    """
    product = models.ForeignKey(
        ProductModel,
        verbose_name=_("Product"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    video = models.FileField(
        verbose_name=_('Video'),
        upload_to="videos/",
        validators=[
            FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'mkv', 'wmv', 'flv'])
        ]
    )

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = _("Product Video")
        verbose_name_plural = _("Product Videos")
        ordering = ('-created_at',)
