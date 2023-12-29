from django.contrib import admin
from django import forms
from django.utils.html import format_html

from apps.preference.models import MenuModel, PreferenceModel, PageModel, BannerModel, TopTendingProductsModel


class MenuModelForm(forms.ModelForm):
    class Meta:
        model = MenuModel
        exclude = ['created_by', 'updated_by']


class MenuModelAdmin(admin.ModelAdmin):
    form = MenuModelForm
    list_display = ('name', 'type', 'position', 'url_path')
    list_filter = ('type',)


admin.site.register(MenuModel, MenuModelAdmin)


class PreferenceModelForm(forms.ModelForm):
    class Meta:
        model = PreferenceModel
        exclude = ['created_by', 'updated_by']


class PreferenceModelAdmin(admin.ModelAdmin):
    form = PreferenceModelForm
    list_display = ('site_name', 'phone', 'email', 'created_at')
    search_fields = ('site_name', 'phone', 'email')


admin.site.register(PreferenceModel, PreferenceModelAdmin)


class PageModelForm(forms.ModelForm):
    class Meta:
        model = PageModel
        exclude = ['created_by', 'updated_by']


class PageModelAdmin(admin.ModelAdmin):
    form = PageModelForm
    list_display = ('title', 'slug', 'created_at')
    search_fields = ('title', 'slug')


admin.site.register(PageModel, PageModelAdmin)


class BannerAdmin(admin.ModelAdmin):
    list_display = ('uuid_last_5_digits', 'preview_image', 'url_path', 'is_active')
    list_filter = ('is_active',)
    readonly_fields = ('preview',)
    exclude = ('created_by', 'updated_by')

    def uuid_last_5_digits(self, obj):
        return str(obj.uuid)[-5:]

    uuid_last_5_digits.short_description = 'UUID (Last 5 digits)'

    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="300" />', obj.image.url)
        return ''

    preview_image.short_description = 'Image Preview'

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="500" />', obj.image.url)
        return ''

    preview.allow_tags = True
    preview.short_description = 'Image Preview'


admin.site.register(BannerModel, BannerAdmin)


class TopTendingProductsAdmin(admin.ModelAdmin):
    exclude = ('created_by', 'updated_by')
    list_display = ('uuid_last_5_digits', 'display_products', 'total_product_count')

    def uuid_last_5_digits(self, obj):
        return str(obj.uuid)[-5:]

    uuid_last_5_digits.short_description = 'UUID (Last 5 digits)'

    def display_products(self, obj):
        return ", ".join([str(product) for product in obj.products.all()])

    display_products.short_description = 'Products'

    def total_product_count(self, obj):
        return obj.products.count()

    total_product_count.short_description = 'Total Products'

    def save_model(self, request, obj, form, change):
        # Ensure only one instance of TopTendingProductsModel exists
        existing_instance = TopTendingProductsModel.objects.first()
        if existing_instance and obj != existing_instance:
            obj.pk = existing_instance.pk
        super().save_model(request, obj, form, change)


admin.site.register(TopTendingProductsModel, TopTendingProductsAdmin)
