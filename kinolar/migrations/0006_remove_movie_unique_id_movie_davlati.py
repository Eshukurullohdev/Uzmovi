# Generated by Django 5.0.4 on 2025-03-23 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinolar', '0005_movie_unique_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='unique_id',
        ),
        migrations.AddField(
            model_name='movie',
            name='davlati',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
