from django.shortcuts import render
from django.http import HttpResponse
from equipment.models import Switch, Description


# Create your views here.

def index(request):
    return render(request, 'equipment/index.html')


def equipment(request):
    switches = Switch.objects.all()
    descriptions = Description.objects.all()
    context = {
        'switches': switches,
        'descriptions': descriptions,
    }
    return render(request, 'equipment/equipment.html', context)

