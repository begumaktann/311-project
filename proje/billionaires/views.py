from django.shortcuts import render
from .models import billionaires_personal,billionaireship  # Import your model
from django.core.paginator import Paginator


# Create your views here.

def home(request):
    return render(request, 'main.html')

def geog(request):
    return render(request, 'geog.html')



def personal(request):
    # Retrieve data from billionaires_personal model
    billionaires_data = billionaires_personal.objects.all().values()  # Fetch all data, adjust as needed
    paginator = Paginator(billionaires_data, 6)  # Display 5 items per page
    page_number = request.GET.get('page')
    page_billionaires = paginator.get_page(page_number)
    context = {
        'billionaires_data': billionaires_data, "page_billionaires":page_billionaires # Pass the data to the template
    }
    return render(request, 'personal.html', context)


def financial(request):
    billionaires_data = billionaireship.objects.all().values()  # Fetch all data, adjust as needed
    paginator = Paginator(billionaires_data, 6)  # Display 5 items per page
    page_number = request.GET.get('page')
    page_billionaires = paginator.get_page(page_number)
    context = {
        'billionaires_data': billionaires_data,"page_billionaires":page_billionaires  # Pass the data to the template
    }

    return render(request, 'financial.html', context)


