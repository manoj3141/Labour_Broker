# Generated by Django 4.2.3 on 2023-07-21 01:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Labour_Broker", "0010_alter_labour_data_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="labour_data",
            name="contact",
            field=models.IntegerField(default=0),
        ),
    ]