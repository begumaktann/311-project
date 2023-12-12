from django.shortcuts import render
from .models import billionaires_personal,billionaireship  # Import your model


# Create your views here.

def home(request):
    return render(request, 'main.html')

def geog(request):
    return render(request, 'geog.html')



def personal(request):
    # Retrieve data from billionaires_personal model
    billionaires_data = billionaires_personal.objects.all()  # Fetch all data, adjust as needed
    print(billionaires_data)
    context = {
        'billionaires_data': billionaires_data  # Pass the data to the template
    }
    return render(request, 'personal.html', context)


def financial(request):
    billionaires_data = billionaireship.objects.all()  # Fetch all data, adjust as needed

    context = {
        'billionaires_data': billionaires_data  # Pass the data to the template
    }

    return render(request, 'financial.html', context)


