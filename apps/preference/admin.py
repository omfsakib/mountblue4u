from django.contrib import admin
from django import forms
from apps.preference.models import MenuModel, PreferenceModel, PageModel


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