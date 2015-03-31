# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0010_auto_20150331_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='updated_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 31, 20, 56, 38, 341000, tzinfo=utc), verbose_name=b'Time Updated'),
            preserve_default=True,
        ),
    ]
