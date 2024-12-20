from django.shortcuts import get_object_or_404, render
from .models import ChaiVariety

# Create your views here.

def home(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'pass_test_app/index.html' , {'chais': chais})

def chai_detail(request, id):
    chai = get_object_or_404(ChaiVariety, id=id)
    return render(request, 'pass_test_app/description.html', {'chai':chai} )