from django.shortcuts import render
from django.http import HttpResponse
from equipment.models import Switch
from equipment.models import Description
# Create your views here.

def index(request):
    return render(request, 'equipment/index.html')


def equipment(request):
    switches = Switch.objects.all()
    context = {
        'switches': switches,
    }
    return render(request, 'equipment/equipment.html', context)

def switch111(request, switch_id=1):
    return render(request, 'equipment/equipment.html', {'switch1': Switch.objects.get(id=switch_id), 'description': Description.objects.filter(descr_switch_id=switch_id)})
