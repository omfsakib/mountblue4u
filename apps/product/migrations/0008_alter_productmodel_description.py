# Generated by Django 5.0 on 2023-12-27 05:47

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_productmodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Description'),
        ),
    ]
