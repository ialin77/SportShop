# Generated by Django 4.2.2 on 2023-08-22 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('shipped', 'shipped'), ('ordered', 'ordered')], default='ordered', max_length=20),
        ),
    ]
