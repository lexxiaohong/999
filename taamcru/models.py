# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class GunDamTable(models.Model):
    name = models.CharField(max_length=50)
    hp = models.IntegerField()