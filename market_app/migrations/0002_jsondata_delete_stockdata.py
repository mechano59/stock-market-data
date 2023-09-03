# Generated by Django 4.2.4 on 2023-09-03 19:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("market_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="JSONData",
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
                ("date", models.DateField()),
                ("trade_code", models.CharField(max_length=20)),
                ("high", models.FloatField()),
                ("low", models.FloatField()),
                ("open", models.FloatField()),
                ("close", models.FloatField()),
                ("volume", models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name="StockData",
        ),
    ]
