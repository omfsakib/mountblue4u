from django import forms
from django.contrib import admin
from django.utils.html import format_html

from apps.promotion.models import DeliveryChargeModel, CouponModel, CampaignModel


# Register your models here.
class DeliveryChargeModelForm(forms.ModelForm):
    class Meta:
        model = DeliveryChargeModel
        exclude = ['created_by', 'updated_by']


class DeliveryChargeModelAdmin(admin.ModelAdmin):
    form = DeliveryChargeModelForm
    list_display = ('inside_fee', 'outside_fee', 'discount', 'created_at')
    search_fields = ('inside_fee', 'outside_fee', 'discount')

admin.site.register(DeliveryChargeModel, DeliveryChargeModelAdmin)



class CouponModelForm(forms.ModelForm):
    class Meta:
        model = CouponModel
        exclude = ['created_by', 'updated_by','use_count']

class CouponModelAdmin(admin.ModelAdmin):
    form = CouponModelForm
    list_display = ('coupon_code', 'amount', 'use_count', 'expire_date', 'created_at')
    search_fields = ('coupon_code', 'amount', 'use_count', 'expire_date')

admin.site.register(CouponModel, CouponModelAdmin)


class CampaignAdmin(admin.ModelAdmin):
    list_display = ('title', 'starts_with', 'preview_image', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'starts_with')
    exclude = ('created_by', 'updated_by')
    readonly_fields = ('preview',)

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="200" />', obj.image.url)
        return ''

    preview.allow_tags = True
    preview.short_description = 'Image Preview'

    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />', obj.image.url)
        return ''

    preview_image.short_description = 'Image Preview'

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'image':
            formfield.widget.can_preview = True  # Allow image preview in form
        return formfield


admin.site.register(CampaignModel, CampaignAdmin)