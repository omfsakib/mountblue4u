from django import forms
from django.contrib import admin
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse, path
from django.utils.html import format_html
from django.utils.translation import gettext as _

from apps.product.models import SizeModel, ColorModel
from apps.sales.models import Order, OrderItem, Wishlist
from apps.user.models import User


# Register your models here.

class PriceRangeFilter(admin.SimpleListFilter):
    title = _('Price Range')
    parameter_name = 'price_range'

    def lookups(self, request, model_admin):
        return (
            ('0-999', _('0 - 999')),
            ('1000`-2999', _('1000 - 2999')),
            ('3000-10000', _('3000 - 9999')),
            # Add more ranges as needed
        )

    def queryset(self, request, queryset):
        if self.value() == '0-100':
            return queryset.filter(total__range=(0, 100))
        elif self.value() == '101-200':
            return queryset.filter(total__range=(101, 200))
        elif self.value() == '201-300':
            return queryset.filter(total__range=(201, 300))
        # Add more conditions as needed
        return queryset


class CustomOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['created_by', 'updated_by', 'is_active', 'coupon_code', 'coupon_amount', 'transaction_id', 'method',
                   'complete']

    def clean(self):
        cleaned_data = super().clean()
        # Add any additional cleaning logic if needed
        return cleaned_data


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product', 'quantity', 'price', 'total', 'order_size', 'order_color']
    exclude = ['created_by', 'updated_by', 'is_active', 'size', 'color']

    def order_size(self, instance):
        return SizeModel.objects.get(uuid=instance.size) if instance.size else ''

    def order_color(self, instance):
        return ColorModel.objects.get(uuid=instance.color) if instance.color else ''


@admin.register(Order)
class CustomOrderAdmin(admin.ModelAdmin):
    form = CustomOrderForm
    list_display = (
        'uuid_last_5_digits', 'customer', 'status', 'total', 'due', 'advance', 'created_at', 'invoice_button')
    search_fields = ['uuid', 'customer__phone', 'status']
    inlines = [OrderItemInline]
    list_filter = ['status', PriceRangeFilter, 'created_at']

    def get_queryset(self, request):
        # Fetch the default queryset
        queryset = super().get_queryset(request)
        # Exclude orders where complete is False
        return queryset.exclude(complete=False)

    def uuid_last_5_digits(self, obj):
        return str(obj.uuid)[-5:]

    uuid_last_5_digits.short_description = 'UUID (Last 5 digits)'

    def invoice_button(self, obj):
        return format_html('<a class="button" href="{}">Invoice</a>',
                           reverse('admin:generate-invoice', args=[obj.uuid]))

    invoice_button.short_description = 'Invoice'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('generate-invoice/<uuid:order_uuid>/', self.generate_invoice, name='generate-invoice'),
        ]
        return custom_urls + urls

    def generate_invoice(self, request, order_uuid):
        # Your logic for generating and displaying the invoice
        pass


admin.site.register(Wishlist)