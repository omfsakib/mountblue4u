from django import forms
from django.contrib import admin

from apps.blog.models import BlogModel


# Register your models here.
class BlogModelForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        exclude = ['created_by', 'updated_by','view_count']


class BlogModelAdmin(admin.ModelAdmin):
    form = BlogModelForm
    list_display = ('title', 'view_count', 'created_at', 'updated_at')
    search_fields = ('title',)

admin.site.register(BlogModel, BlogModelAdmin)
