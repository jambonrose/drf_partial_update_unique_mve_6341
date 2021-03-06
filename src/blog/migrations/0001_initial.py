# Generated by Django 2.1.3 on 2018-11-28 15:47

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=63)),
                ("slug", models.SlugField(max_length=63)),
                ("pub_date", models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name="UniquePost",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=63)),
                ("slug", models.SlugField(max_length=63, unique_for_month="pub_date")),
                ("pub_date", models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
