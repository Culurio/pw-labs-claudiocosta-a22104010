# Generated by Django 4.0.4 on 2022-05-21 18:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('linkdin', models.URLField()),
                ('portfolio', models.URLField()),
                ('github', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('linkdin', models.URLField()),
                ('lusofona_url', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('year', models.IntegerField(default=0)),
                ('etcs', models.IntegerField(default=0)),
                ('semester', models.IntegerField(default=0)),
                ('school_year', models.IntegerField(default=0)),
                ('rank', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('topics', models.CharField(max_length=100)),
                ('students', models.ManyToManyField(blank=True, to='portfolio.student')),
                ('teacher', models.ManyToManyField(blank=True, to='portfolio.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('year', models.IntegerField(default=0)),
                ('github', models.URLField()),
                ('video_url', models.URLField()),
                ('tech', models.URLField()),
                ('skills', models.CharField(max_length=500)),
                ('participants', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.student')),
            ],
        ),
    ]
