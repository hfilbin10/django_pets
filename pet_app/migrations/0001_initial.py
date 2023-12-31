# Generated by Django 4.2.7 on 2023-11-21 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bird',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField()),
                ('vaccinated', models.BooleanField(default=True)),
                ('description', models.CharField(max_length=255)),
                ('species', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField()),
                ('vaccinated', models.BooleanField(default=True)),
                ('description', models.TextField()),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=255)),
                ('vaccinated', models.BooleanField(default=True)),
                ('breed', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Exotic_animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_of_origin', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField()),
                ('type_of_animal', models.CharField(max_length=255)),
                ('vaccinated', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField()),
                ('number_of_pets', models.IntegerField()),
            ],
        ),
    ]
