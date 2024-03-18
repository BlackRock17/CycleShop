# Generated by Django 4.2.11 on 2024-03-16 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("components", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="components",
            name="quantity",
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name="ComponentsInventory",
        ),
    ]