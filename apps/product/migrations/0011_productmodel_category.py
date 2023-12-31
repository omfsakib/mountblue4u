# Generated by Django 4.2.8 on 2023-12-29 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_productmodel_sell_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_products', to='product.categorymodel', verbose_name='Category'),
        ),
    ]