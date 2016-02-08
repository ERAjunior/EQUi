from django.conf.urls import url
from equipment import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^equipment/$', views.equipment, name='equipment'),
]