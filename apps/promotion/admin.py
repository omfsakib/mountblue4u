from django import forms
from django.contrib import admin

from apps.promotion.models import DeliveryChargeModel, CouponModel


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