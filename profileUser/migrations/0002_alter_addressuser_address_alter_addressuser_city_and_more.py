# Generated by Django 4.2.14 on 2024-09-11 13:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profileUser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addressuser',
            name='address',
            field=models.TextField(max_length=500, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='addressuser',
            name='city',
            field=models.CharField(max_length=100, verbose_name='شهر'),
        ),
        migrations.AlterField(
            model_name='addressuser',
            name='full_name',
            field=models.CharField(max_length=100, verbose_name='نام کامل'),
        ),
        migrations.AlterField(
            model_name='addressuser',
            name='license_plate',
            field=models.CharField(max_length=20, verbose_name='پلاک'),
        ),
        migrations.AlterField(
            model_name='addressuser',
            name='phone',
            field=models.CharField(max_length=11, verbose_name='شماره تلفن'),
        ),
        migrations.AlterField(
            model_name='addressuser',
            name='postal_code',
            field=models.CharField(max_length=10, verbose_name='کد پستی'),
        ),
        migrations.AlterField(
            model_name='addressuser',
            name='province',
            field=models.CharField(max_length=50, verbose_name='استان'),
        ),
        migrations.AlterField(
            model_name='addressuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]
