# Generated by Django 5.1.5 on 2025-04-28 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GrabFood', '0023_alter_history_customer_alter_history_menu_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(default='images/default_image.jpg', upload_to='images/'),
        ),
    ]
