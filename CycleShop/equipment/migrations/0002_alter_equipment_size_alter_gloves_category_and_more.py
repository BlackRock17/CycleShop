# Generated by Django 4.2.11 on 2024-04-04 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("equipment", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="equipment",
            name="size",
            field=models.CharField(
                choices=[("S", "S"), ("M", "M"), ("L", "L"), ("XL", "XL")],
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="gloves",
            name="category",
            field=models.CharField(
                choices=[
                    ("Long Finger Gloves", "Long Finger Gloves"),
                    ("Short Finger Gloves", "Short Finger Gloves"),
                    ("Winter Gloves", "Winter Gloves"),
                ],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="protection",
            name="category",
            field=models.CharField(
                choices=[
                    ("Knee Pads", "Knee Pads"),
                    ("Elbow Pads", "Elbow Pads"),
                    ("Neck Protectors", "Neck Protectors"),
                    ("Body Protectors", "Body Protectors"),
                    ("Protectors Set", "Protectors Set"),
                ],
                max_length=50,
            ),
        ),
    ]