# Generated by Django 3.2 on 2021-04-26 13:23

import audioapp.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudioBooks',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('duration', models.PositiveIntegerField()),
                ('uploaded_time', models.DateTimeField(validators=[audioapp.models.validate_uploaded_time])),
                ('author', models.CharField(max_length=100)),
                ('narrator', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('duration', models.PositiveIntegerField()),
                ('uploaded_time', models.DateTimeField(validators=[audioapp.models.validate_uploaded_time])),
                ('host', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('duration', models.PositiveIntegerField()),
                ('uploaded_time', models.DateTimeField(validators=[audioapp.models.validate_uploaded_time])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ListOfMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=100)),
                ('podcast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audioapp.podcast')),
            ],
        ),
    ]
