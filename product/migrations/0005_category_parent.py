# Generated by Django 5.0.6 on 2024-09-09 15:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0004_remove_productfeature_feature_productfeature_key_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="subs",
                to="product.category",
                verbose_name="include",
            ),
        ),
    ]
