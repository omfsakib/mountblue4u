# Generated by Django 4.2.8 on 2023-12-29 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preference', '0005_alter_menumodel_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menumodel',
            options={'ordering': ('position',), 'verbose_name': 'Menu', 'verbose_name_plural': 'Menus'},
        ),
    ]