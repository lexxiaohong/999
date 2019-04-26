# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class TopicTable(models.Model):

    room_id = models.IntegerField()
    topic = models.CharField(max_length=50)
    content = models.CharField(max_length=50)