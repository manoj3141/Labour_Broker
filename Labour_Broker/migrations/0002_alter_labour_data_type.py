# Generated by Django 4.2.3 on 2023-07-16 07:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Labour_Broker", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="labour_data",
            name="type",
            field=models.CharField(
                choices=[
                    ("agriculture", "agriculture"),
                    ("construction", "construction"),
                ],
                max_length=100,
            ),
        ),
    ]
