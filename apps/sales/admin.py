from django import forms
from django.contrib import admin
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse, path
from django.utils.html import format_html

from apps.sales.models import Order, OrderItem
from apps.user.models import User


# Register your models here.
class CustomOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['created_by', 'updated_by', 'is_active','coupon_code','coupon_amount','transaction_id', 'method','complete']

    def clean(self):
        cleaned_data = super().clean()
        # Add any additional cleaning logic if needed
        return cleaned_data



class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1
    readonly_fields = ['product', 'quantity', 'price', 'total','size', 'color']
    exclude = ['created_by', 'updated_by', 'is_active']

@admin.register(Order)
class CustomOrderAdmin(admin.ModelAdmin):
    form = CustomOrderForm
    list_display = ('uuid_last_5_digits', 'customer', 'status', 'created_at', 'invoice_button')
    search_fields = ['uuid', 'customer__username', 'status']
    inlines = [OrderItemInline]

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