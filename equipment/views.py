from django.shortcuts import render
from django.http import HttpResponse
from equipment.models import Switch
# Create your views here.

def index(request):
    return render(request, 'equipment/index.html')


def equipment(request):
    switches = Switch.objects.all()
    context = {
        'switches': switches
    }
    return render(request, 'equipment/equipment.html', context,)