from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'equipment/index.html')

def equipment(request):
    return render(request, 'equipment/equipment.html')