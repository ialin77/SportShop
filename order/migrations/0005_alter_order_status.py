# Generated by Django 4.2.2 on 2023-09-18 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('shipped', 'shipped'), ('ordered', 'ordered')], default='ordered', max_length=20),
        ),
    ]
