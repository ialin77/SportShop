# Generated by Django 4.2.2 on 2023-08-22 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_category_options_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='thumbnail',
        ),
    ]