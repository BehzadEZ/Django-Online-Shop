# Generated by Django 5.0.6 on 2024-07-26 14:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0003_initial"),
        ("admin", "0003_logentry_add_action_flag_choices"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="User",
            new_name="MyUser",
        ),
    ]