# Generated by Django 4.2.14 on 2024-09-12 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_address_city_address_license_plate_address_province'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
