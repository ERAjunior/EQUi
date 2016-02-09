from django.contrib import admin

# Register your models here.
from equipment.models import Area, Street, House, VendorModel, SwitchModel, Switch

class SwitchInHouse(admin.StackedInline):
    model = Switch
    extra = 1

class HouseAdmin(admin.ModelAdmin):
    inlines = [SwitchInHouse]

admin.site.register([Area,Street,VendorModel, SwitchModel, Switch])
admin.site.register(House, HouseAdmin)


