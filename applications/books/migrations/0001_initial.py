# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 20:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('taken', models.BooleanField(default=False)),
                ('taker', models.CharField(blank=True, max_length=20)),
                ('last_take', models.DateField(blank=True)),
                ('author', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('books', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='collection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Collection'),
        ),
    ]
