# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Feed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='descripcion',
            field=models.CharField(default=b'Sin descripcion', max_length=1200),
        ),
    ]
