from django.contrib import admin

# Register your models here.
from equipment.models import Area, Street, House, VendorModel, SwitchModel, Switch, Description

class SwitchInHouse(admin.StackedInline):
    model = Switch
    extra = 1

class HouseAdmin(admin.ModelAdmin):
    inlines = [SwitchInHouse]

class SwitchInLine(admin.StackedInline):
    model = Description
    extra = 0
    fields = [('descr_FIO','descr_port','descr_kv','descr_pd'),'user']

class SwitchAdmin(admin.ModelAdmin):
    inlines = [SwitchInLine]


admin.site.register([Area,Street,VendorModel, SwitchModel])
admin.site.register(House, HouseAdmin)
admin.site.register(Switch, SwitchAdmin)

