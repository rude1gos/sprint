# Generated by Django 4.2.1 on 2023-05-10 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('height', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PerevalAreas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_parent', models.IntegerField()),
                ('title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PerevalImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='uploads/')),
                ('image_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('otc', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PerevalAdded',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beauty_title', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('other_title', models.CharField(max_length=255)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('winter_level', models.CharField(max_length=100)),
                ('spring_level', models.CharField(max_length=100)),
                ('summer_level', models.CharField(max_length=100)),
                ('autumn_level', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('new', 'новый'), ('pending', 'модератор взял в работу'), ('accepted', 'модерация прошла успешно'), ('rejected', 'модерация прошла, информация не принята')], default='new', max_length=8)),
                ('coord_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pereval.coords')),
                ('images', models.ManyToManyField(to='pereval.perevalimages')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pereval.users')),
            ],
        ),
    ]
