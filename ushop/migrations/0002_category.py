# Generated by Django 4.2.6 on 2024-05-22 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ushop", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("category_image", models.ImageField(upload_to="uploads/category/")),
                (
                    "category_name",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
            ],
        ),
    ]
