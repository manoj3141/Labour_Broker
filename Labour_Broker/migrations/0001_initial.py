# Generated by Django 4.2.3 on 2023-07-13 02:29

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Labour_data",
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
                ("type", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=100)),
                ("no_of_w", models.IntegerField()),
                ("salary", models.IntegerField()),
                ("location", models.CharField(max_length=100)),
            ],
        ),
    ]
