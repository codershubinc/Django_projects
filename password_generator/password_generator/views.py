from django.shortcuts import render


def home(request):
    return render(request, 'password_generator/index.html')  