# Generated by Django 4.2.3 on 2023-07-17 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("Labour_Broker", "0004_labour_data_contact"),
    ]

    operations = [
        migrations.CreateModel(
            name="Labour_type",
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
                ("reg_type", models.CharField(max_length=30)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Labour_Broker.labour_data",
                    ),
                ),
            ],
        ),
    ]
