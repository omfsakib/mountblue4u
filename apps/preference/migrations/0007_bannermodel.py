# Generated by Django 4.2.8 on 2023-12-29 13:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('preference', '0006_alter_menumodel_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerModel',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='uuid')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at?')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at?')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active?')),
                ('image', models.ImageField(upload_to='banners/', verbose_name='Image')),
                ('url_path', models.CharField(blank=True, max_length=255, null=True, verbose_name='URL path')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Banners',
                'ordering': ('-created_at',),
            },
        ),
    ]