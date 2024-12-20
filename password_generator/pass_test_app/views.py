from django.shortcuts import render
from .models import ChaiVariety

# Create your views here.

def home(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'pass_test_app/index.html' , {'chais': chais})