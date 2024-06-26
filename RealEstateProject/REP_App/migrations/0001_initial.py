# Generated by Django 4.2.6 on 2023-12-04 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="property_profile",
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
                ("property_name", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=50)),
                (
                    "unit_type",
                    models.CharField(
                        choices=[
                            ("1BHK", "1BHK"),
                            ("2BHK", "2BHK"),
                            ("3BHK", "3BHK"),
                            ("4BHK", "4BHK"),
                        ],
                        max_length=4,
                    ),
                ),
                ("rent", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="tenant_profile",
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
                ("tenant_name", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=255)),
                (
                    "unit_type",
                    models.CharField(
                        choices=[
                            ("1BHK", "1BHK"),
                            ("2BHK", "2BHK"),
                            ("3BHK", "3BHK"),
                            ("4BHK", "4BHK"),
                        ],
                        max_length=4,
                    ),
                ),
                ("document", models.TextField()),
                (
                    "property",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="REP_App.property_profile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="tenant_rental_info",
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
                ("agreementend_date", models.DateField()),
                ("monthly_rent", models.DecimalField(decimal_places=2, max_digits=10)),
                ("monthly_rent_date", models.DateField()),
                (
                    "tenant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="REP_App.tenant_profile",
                    ),
                ),
            ],
        ),
    ]
