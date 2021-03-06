# Generated by Django 3.1.7 on 2021-06-05 03:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_box_office_anime_champion_year_box_office_champion_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Box_office_opening_first_week',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=20)),
                ('days', models.CharField(max_length=10)),
                ('box_office', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=20)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Box_office_opening_first_week_anime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=20)),
                ('days', models.CharField(max_length=10)),
                ('box_office', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=20)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Box_office_opening_first_week_local',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=20)),
                ('days', models.CharField(max_length=10)),
                ('box_office', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=20)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
