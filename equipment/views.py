from django.shortcuts import render
from django.http import HttpResponse
from equipment.models import Switch
from equipment.models import Area
# Create your views here.

def index(request):
    return render(request, 'equipment/index.html')


def equipment(request):
    switches = Switch.objects.all()
    areas = Area.objects.all()
    context = {
        'switches': switches,
        'areas': areas
    }
    return render(request, 'equipment/equipment.html', context,)