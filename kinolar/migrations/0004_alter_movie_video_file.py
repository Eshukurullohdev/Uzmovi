# Generated by Django 5.0.4 on 2025-03-23 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinolar', '0003_remove_movie_poster_movie_video_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]
