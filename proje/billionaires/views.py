from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'main.html')

def geog(request):
    return render(request, 'geog.html')

def personal(request):
    return render(request, 'personal.html')

def financial(request):
    return render(request, 'financial.html')

