# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-06 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SIP_generator_web', '0005_auto_20170706_0021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metadata',
            name='accessConditions',
        ),
        migrations.RemoveField(
            model_name='metadata',
            name='creationDates',
        ),
        migrations.RemoveField(
            model_name='metadata',
            name='creationDatesEnd',
        ),
        migrations.RemoveField(
            model_name='metadata',
            name='creationDatesStart',
        ),
        migrations.RemoveField(
            model_name='metadata',
            name='creationDatesType',
        ),
        migrations.RemoveField(
            model_name='metadata',
            name='creators',
        ),
        migrations.RemoveField(
            model_name='metadata',
            name='extendAndMedium',
        ),
        migrations.RemoveField(
            model_name='metadata',
            name='identifier',
        ),
        migrations.RemoveField(
            model_name='metadata',
            name='language',
        ),
        migrations.RemoveField(
            model_name='metadata',
            name='locationOfOriginals',
        ),
        migrations.RemoveField(
            model_name='metadata',
            name='placeAccessPoints',
        ),
        migrations.RemoveField(
            model_name='metadata',
            name='scopeAndContent',
        ),
        migrations.RemoveField(
            model_name='metadata',
            name='subjectAccessPoint',
        ),
        migrations.AddField(
            model_name='metadata',
            name='_format',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='metadata',
            name='contributor',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='metadata',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='metadata',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='metadata',
            name='filename',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='metadata',
            name='isPartOf',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='metadata',
            name='issued',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='metadata',
            name='notes',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='metadata',
            name='project_website',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='metadata',
            name='publisher',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='metadata',
            name='rights',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='metadata',
            name='subject',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
