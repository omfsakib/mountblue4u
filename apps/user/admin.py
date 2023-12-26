from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.http import Http404

from apps.user.models import User


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        ('Personal info', {'fields': ('name', 'phone', 'avatar')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Role', {'fields': ('role',)}),  # Add the 'role' field to the admin form
    )
    list_display = ('name', 'phone', 'is_staff', 'role')  # Add 'role' to the list display

    def add_view(self, request, form_url='', extra_context=None):
        raise Http404("Page not found")


admin.site.register(User, UserAdmin)
