from django.shortcuts import render
from django.http import HttpResponse
from equipment.models import Switch, Description


# Create your views here.

def index(request):
    return render(request, 'equipment/index.html')


def equipment(request):
    switches = Switch.objects.all()
    context = {
        'switches': switches,
    }
    return render(request, 'equipment/equipment.html', context)


def description(request, switch_id):
    descriptions = Description.objects.filter(descr_switch_id=switch_id)
    switch = Switch.objects.get(id=switch_id)
    context = {
        'descriptions': descriptions,
        'switch': switch
    }
    return render(request, 'equipment/description.html', context)
