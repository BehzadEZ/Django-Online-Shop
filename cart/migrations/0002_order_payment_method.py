# Generated by Django 4.2.14 on 2024-09-14 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(default='انتقال مستقیم بانکی', max_length=100, verbose_name='payment_method'),
        ),
    ]