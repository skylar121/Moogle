# Generated by Django 3.2.13 on 2022-11-17 08:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('tmdb_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('title', models.TextField()),
                ('overview', models.TextField()),
                ('release_date', models.TextField(null=True)),
                ('tmdb_id', models.IntegerField(primary_key=True, serialize=False)),
                ('adult', models.BooleanField()),
                ('popularity', models.FloatField()),
                ('vote_average', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('vote_count', models.IntegerField()),
                ('poster_path', models.TextField(null=True)),
                ('backdrop_path', models.TextField(null=True)),
                ('genres', models.ManyToManyField(to='movies.Genre')),
            ],
        ),
    ]
