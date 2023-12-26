from django.contrib import admin
from django import forms
from apps.preference.models import MenuModel


class MenuModelForm(forms.ModelForm):
    class Meta:
        model = MenuModel
        exclude = ['created_by', 'updated_by']


class MenuModelAdmin(admin.ModelAdmin):
    form = MenuModelForm
    list_display = ('name', 'type', 'position', 'url_path')
    list_filter = ('type',)


admin.site.register(MenuModel, MenuModelAdmin)
