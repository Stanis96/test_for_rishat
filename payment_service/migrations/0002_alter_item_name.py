# Generated by Django 4.1.3 on 2022-11-25 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payment_service", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="name",
            field=models.CharField(max_length=100),
        ),
    ]
