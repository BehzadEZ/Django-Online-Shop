# Generated by Django 4.2.14 on 2024-09-10 13:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=11, verbose_name='phone_number')),
                ('province', models.CharField(max_length=50, verbose_name='province')),
                ('license_plate', models.IntegerField(verbose_name='license_plate')),
                ('city', models.CharField(max_length=100, verbose_name='city')),
                ('postal_code', models.CharField(max_length=100, verbose_name='postal_code')),
                ('address', models.TextField(max_length=500, verbose_name='address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]