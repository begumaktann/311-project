from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'main.html')  # Assuming you have a 'home.html' template

def geog(request):
    return render(request, 'geog.html')

def personal(request):
    return render(request, 'personal.html')

def financial(request):
    return render(request, 'financial.html')

def login(request):
    return render(request, 'login.html')
