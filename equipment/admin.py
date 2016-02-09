from django.contrib import admin

# Register your models here.
from equipment.models import Area, Street, House, VendorModel, SwitchModel

admin.site.register([Area,Street,House,VendorModel, SwitchModel])