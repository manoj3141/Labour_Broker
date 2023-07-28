# Generated by Django 4.2.3 on 2023-07-18 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Labour_Broker", "0006_alter_labour_type_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="labour_data",
            name="other_details",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="labour_data",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]