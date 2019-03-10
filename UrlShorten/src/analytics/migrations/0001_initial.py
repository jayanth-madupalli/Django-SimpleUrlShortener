# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2019-01-02 05:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shortener', '0006_shorten_hits'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClickEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('sh_url', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shortener.Shorten')),
            ],
        ),
    ]