# Generated by Django 5.0.1 on 2024-01-23 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0004_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
