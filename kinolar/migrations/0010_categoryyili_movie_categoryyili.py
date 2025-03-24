# Generated by Django 5.0.4 on 2025-03-24 09:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinolar', '0009_categorytili_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryYili',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryyili', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='categoryyili',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kinolar.categoryyili'),
        ),
    ]
