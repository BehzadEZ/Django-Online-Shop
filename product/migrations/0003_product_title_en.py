# Generated by Django 5.0.6 on 2024-08-02 09:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0002_productimage"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="title_en",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
