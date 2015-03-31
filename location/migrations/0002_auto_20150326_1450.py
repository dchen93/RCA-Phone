# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('center_name', models.CharField(max_length=200)),
                ('current_location', models.BooleanField(default=False)),
                ('phone', models.ForeignKey(to='location.Phone')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='computercenter',
            name='phone',
        ),
        migrations.DeleteModel(
            name='ComputerCenter',
        ),
    ]
