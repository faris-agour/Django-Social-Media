# Generated by Django 5.0.3 on 2024-04-17 22:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0004_friendship_accepted"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="friends",
        ),
    ]