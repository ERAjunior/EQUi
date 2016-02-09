# coding=utf-8
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Area(models.Model):
    class Meta():
        db_table = 'area'
        verbose_name = u'Район города '
        verbose_name_plural = u'Районы города'
    name_area = models.CharField(u'Район города', max_length=200)
    date_create_area = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name_area

class Street(models.Model):
    class Meta():
        db_table = 'street'
        verbose_name = u'Улицу'
        verbose_name_plural = u'Улицы'
    name_street = models.CharField(u'Название улицы',max_length=200, default='ул.')
    id_area = models.ForeignKey(Area)
    date_create_street = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name_street

class House(models.Model):
    class Meta():
        db_table = 'house'
        verbose_name = u'Дом'
        verbose_name_plural = u'Дома'
    street_house = models.ForeignKey(Street)
    num_house = models.IntegerField(u'Номер дома',default=1)
    korp_house = models.CharField(u'Корпус',max_length=15, blank=True, default='корп.')
    date_create_house = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        if self.korp_house:
            return u'%s %s/%s' % (self.street_house, self.num_house, self.korp_house)
        else:
            return u'%s %s' % (self.street_house, self.num_house)

