# Generated by Django 5.2.1 on 2025-05-23 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="image",
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
                ("image_name", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="media/")),
                ("date", models.DateField()),
            ],
        ),
    ]
