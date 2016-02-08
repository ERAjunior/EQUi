from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Area(models.Model):
    class Meta():
        db_table = 'area'
    name_area = models.CharField(max_length=200)
    date_create_area = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name_area

class Street(models.Model):
    class Meta():
        db_table = 'street'
    name_street = models.CharField(max_length=200)
    id_area = models.ForeignKey(Area)
    date_create_street = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name_street

class House(models.Model):
    class Meta():
        db_table = 'house'
    street_house = models.ForeignKey(Street)
    num_house = models.IntegerField(default=1)
    korp_house = models.CharField(max_length=4, blank=True)
    date_create_house = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return u'%s %s %s' % (self.street_house, self.num_house, self.korp_house)
