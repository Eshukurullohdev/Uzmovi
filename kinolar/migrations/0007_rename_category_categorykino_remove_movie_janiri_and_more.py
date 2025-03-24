# Generated by Django 5.0.4 on 2025-03-24 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kinolar', '0006_remove_movie_unique_id_movie_davlati'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='CategoryKino',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='janiri',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='category',
        ),
        migrations.RenameField(
            model_name='categorykino',
            old_name='category',
            new_name='categorykino',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
    ]
