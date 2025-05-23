# Generated by Django 5.1.5 on 2025-04-17 06:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GrabFood', '0022_voucher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='histories', to='GrabFood.customer'),
        ),
        migrations.AlterField(
            model_name='history',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='histories', to='GrabFood.menufood'),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_voucher', to='GrabFood.restaurant'),
        ),
    ]
