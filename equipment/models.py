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

    name_street = models.CharField(u'Название улицы', max_length=200, default='ул.')
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
    num_house = models.IntegerField(u'Номер дома', default=1)
    korp_house = models.CharField(u'Корпус', max_length=15, blank=True, default='корп.')
    date_create_house = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        if self.korp_house:
            return u'%s %s/%s' % (self.street_house, self.num_house, self.korp_house)
        else:
            return u'%s %s' % (self.street_house, self.num_house)


class VendorModel(models.Model):
    class Meta():
        db_table = 'vendor_model'
        verbose_name = u'Производитель'
        verbose_name_plural = u'Производители'

    vendor_name = models.CharField(u'Производитель', max_length=200)
    date_create_vendor = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.vendor_name


class SwitchModel(models.Model):
    class Meta():
        db_table = 'switch_model'
        verbose_name = u'Модель'
        verbose_name_plural = u'Модели'

    vendor_model = models.ForeignKey(VendorModel)
    name_model = models.CharField(u'Название модели', max_length=200)
    num_ports_model = models.IntegerField(u'Кол-во портов', default=1)
    num_watt_model = models.IntegerField(u'Потребляемая мощность в Вт', default=1)
    date_create_model = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return u'%s - %s' % (self.vendor_model, self.name_model)


class Switch(models.Model):
    class Meta():
        db_table = 'switch'
        verbose_name = u'Коммутатор'
        verbose_name_plural = u'Коммутаторы'

    name_switch = models.CharField(u'Обозначение на сети', max_length=100)
    ipaddr_switch = models.GenericIPAddressField(default='0.0.0.0')
    pd_switch = models.CharField(max_length=100, default='пд.', blank=True, null=True)
    switch_modelid = models.ForeignKey(SwitchModel, null=True)
    switch_house = models.ForeignKey(House, null=True)
    date_create_switch = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, null=True)

    def __unicode__(self):
        if self.pd_switch:
            return u'%s - %s - %s (%s)' % (self.ipaddr_switch, self.name_switch, self.switch_house, self.pd_switch)
        else:
            return u'%s - %s - %s' % (self.ipaddr_switch, self.name_switch, self.switch_house)


class Description(models.Model):
    class Meta():
        db_table = 'description'
        verbose_name = u'Дескрипшен'
        verbose_name_plural = u'Дескрипшены'

    descr_switch = models.ForeignKey(Switch)
    descr_kv = models.CharField(u'Квартира', max_length=5)
    descr_pd = models.CharField(u'Подъезд', max_length=5)
    descr_port = models.IntegerField(u'Порт')
    descr_FIO = models.CharField(u'ФИО', max_length=100)
    date_create_descr = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, null=True)
