# Generated by Django 4.1.2 on 2022-10-18 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="img",
            field=models.FileField(blank=True, upload_to="static/images/todos/"),
        ),
    ]
