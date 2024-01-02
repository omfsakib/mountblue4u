from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.utils.html import format_html,linebreaks

from apps.product.models import CategoryModel, SizeModel, ColorModel, ProductVariantModel, ProductImagesModel, \
    ProductVideosModel, ProductModel, ReviewImageModel, ReviewModel


# Register your models here.

class ImagePreviewWidget(forms.ClearableFileInput):
    def render(self, name, value, attrs=None, renderer=None):
        output = super().render(name, value, attrs, renderer)
        if value:
            image_html = format_html('<br><img src="{}" style="max-height: 100px; max-width: 100px;" />', value.url)
            output = format_html('{}{}', output, image_html)
        return output

class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        exclude = ['created_by', 'updated_by']


class CategoryModelAdmin(admin.ModelAdmin):
    form = CategoryModelForm
    list_display = ('name', 'display_image', 'is_featured')
    list_filter = ('is_featured',)
    search_fields = ('name',)

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.image.url))
        return ''

    display_image.short_description = 'Image Preview'


admin.site.register(CategoryModel, CategoryModelAdmin)


class SizeModelForm(forms.ModelForm):
    class Meta:
        model = SizeModel
        exclude = ['created_by', 'updated_by']


class SizeModelAdmin(admin.ModelAdmin):
    form = SizeModelForm
    list_display = ('name', 'created_at', 'updated_at')  # Adjust as needed
    search_fields = ('name',)  # Enable search for the 'name' field


admin.site.register(SizeModel, SizeModelAdmin)


class ColorModelForm(forms.ModelForm):
    class Meta:
        model = ColorModel
        exclude = ['created_by', 'updated_by']


class ColorModelAdmin(admin.ModelAdmin):
    form = ColorModelForm
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)


admin.site.register(ColorModel, ColorModelAdmin)


class ProductVariantInline(admin.TabularInline):
    model = ProductVariantModel
    extra = 1
    exclude = ['created_by', 'updated_by']


class MediaPreviewWidget(forms.ClearableFileInput):
    def render(self, name, value, attrs=None, renderer=None):
        output = super().render(name, value, attrs, renderer)
        if value:
            media_html = format_html('<br><{} src="{}" style="max-height: 100px; max-width: 100px;" />',
                                     'img' if name.endswith('image') else 'video', value.url)
            output = format_html('{}{}', output, media_html)
        return output

class ProductMediaForm(forms.ModelForm):
    class Meta:
        exclude = ['created_by', 'updated_by']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.ClearableFileInput):
                field.widget = MediaPreviewWidget(attrs={'class': 'vImageField'})

class ProductImagesInline(admin.TabularInline):
    model = ProductImagesModel
    form = ProductMediaForm
    extra = 1
    exclude = ['created_by', 'updated_by']

class ProductVideosInline(admin.TabularInline):
    model = ProductVideosModel
    form = ProductMediaForm
    extra = 1
    exclude = ['created_by', 'updated_by']



class ProductModelForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        exclude = ['created_by', 'updated_by','rating', 'sell_count']


class ProductModelAdmin(admin.ModelAdmin):
    form = ProductModelForm
    inlines = [ProductVariantInline, ProductImagesInline, ProductVideosInline]
    list_display = ('title', 'stock', 'rating', 'price', 'discount_amount')
    search_fields = ('title',)

    def stock(self, obj):
        # Customize this method to generate the desired stock information
        variants = obj.product_variants.all()  # Assuming the related name is set to 'productvariantmodel_set'
        stock_info = "\n".join(f"({variant.size} - {variant.color}) - {variant.stock}" for variant in variants)
        return format_html(linebreaks(stock_info))

    stock.short_description = 'Stock'


admin.site.register(ProductModel, ProductModelAdmin)


class ReviewImageForm(forms.ModelForm):
    class Meta:
        model = ReviewImageModel
        exclude = ['created_by', 'updated_by']

    image = forms.ImageField(widget=ImagePreviewWidget)

class ReviewImageInline(admin.TabularInline):
    model = ReviewImageModel
    extra = 1
    form = ReviewImageForm
    exclude = ['created_by', 'updated_by']


class ReviewModelForm(forms.ModelForm):
    class Meta:
        model = ReviewModel
        exclude = ['created_by', 'updated_by']

class ReviewModelAdmin(admin.ModelAdmin):
    form = ReviewModelForm
    list_display = ('comment', 'rate', 'product', 'user', 'created_at')
    inlines = [ReviewImageInline]

admin.site.register(ReviewModel, ReviewModelAdmin)

admin.site.unregister(Group)