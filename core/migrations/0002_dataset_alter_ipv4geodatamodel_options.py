# Generated by Django 5.1.4 on 2024-12-08 16:11

import django_prometheus.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('alias', models.TextField()),
            ],
            bases=(django_prometheus.models.ExportModelOperationsMixin('dataset'), models.Model),
        ),
        migrations.AlterModelOptions(
            name='ipv4geodatamodel',
            options={'verbose_name': 'IPv4GeoModel', 'verbose_name_plural': 'IPv4GeoModels'},
        ),
    ]