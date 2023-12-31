# Generated by Django 5.0 on 2023-12-27 08:12

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CouponModel',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='uuid')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at?')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at?')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active?')),
                ('coupon_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='Coupon Code')),
                ('amount', models.FloatField(default=0, verbose_name='Amount')),
                ('use_count', models.PositiveSmallIntegerField(default=0, verbose_name='Use Count')),
                ('expire_date', models.DateTimeField(blank=True, null=True, verbose_name='Expire Date')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'verbose_name': 'Coupon Code',
                'verbose_name_plural': 'Coupon Codes',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='DeliveryChargeModel',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='uuid')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at?')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at?')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active?')),
                ('inside_fee', models.FloatField(default=0, verbose_name='Inside City Fee')),
                ('outside_fee', models.FloatField(default=0, verbose_name='Outside City Fee')),
                ('discount', models.IntegerField(default=0, verbose_name='Discount')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL, verbose_name='Updated by')),
            ],
            options={
                'verbose_name': 'Delivery Charge',
                'verbose_name_plural': 'Delivery Charge',
                'ordering': ('-created_at',),
            },
        ),
    ]
