# Generated by Django 3.0.7 on 2020-07-19 12:47

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0019_auto_20200719_0627'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='attributes',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
    ]
