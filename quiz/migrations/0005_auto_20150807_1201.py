# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20150807_0904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='image',
        ),
        migrations.AddField(
            model_name='question',
            name='image_link',
            field=models.CharField(default=b'/static/photos/default-image.jpg', max_length=100),
        ),
    ]
