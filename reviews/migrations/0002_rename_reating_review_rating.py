# Generated by Django 4.2.1 on 2023-05-15 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="review",
            old_name="reating",
            new_name="rating",
        ),
    ]
