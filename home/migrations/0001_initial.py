# Generated by Django 5.0.6 on 2024-08-26 15:33

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="advimgage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("advertize_image", models.ImageField(upload_to="media")),
                ("title_adv_img", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="slider",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("imagename", models.ImageField(upload_to="media")),
                ("title_img", models.CharField(max_length=200)),
            ],
        ),
    ]