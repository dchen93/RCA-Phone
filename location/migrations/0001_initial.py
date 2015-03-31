# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComputerCenter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('center_name', models.CharField(max_length=200)),
                ('current_location', models.BooleanField(default=False, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_name', models.CharField(max_length=200)),
                ('updated_time', models.DateTimeField(verbose_name=b'Time Updated')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='computercenter',
            name='phone',
            field=models.ForeignKey(to='location.Phone'),
            preserve_default=True,
        ),
    ]
