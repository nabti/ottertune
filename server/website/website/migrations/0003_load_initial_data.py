# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-12-07 19:51
from __future__ import unicode_literals

from django.core.management import call_command
from django.db import migrations


def load_initial_data(apps, schema_editor):
    initial_data_fixtures = [
        "dbms_catalog.json",
        "hardware.json",
        "postgres-96_knobs.json",
        "postgres-96_metrics.json",
        "postgres-92_knobs.json",
        "postgres-92_metrics.json",
        "postgres-93_knobs.json",
        "postgres-93_metrics.json",
        "postgres-94_knobs.json",
        "postgres-94_metrics.json",
        "myrocks-5.6_knobs.json",
        "myrocks-5.6_metrics.json"
    ]
    for fixture in initial_data_fixtures:
        call_command("loaddata", fixture, app_label="website")


def unload_initial_data(apps, schema_editor):
    model_names = [
        "DBMSCatalog",
        "KnobCatalog",
        "MetricCatalog",
        "Hardware"
    ]
    for model_name in model_names:
        model = apps.get_model("website", model_name)
        model.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_enable_compression'),
    ]

    operations = [
        migrations.RunPython(load_initial_data, unload_initial_data)
    ]