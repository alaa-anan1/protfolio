from django.shortcuts import render
from about_page.models import About , Trip

# Create your views here.
def about_index(request):
    about = About.objects.all()
    context = {
        'about': about 
    }
    return render(request, 'about_index.html', context)

def trip_index(request):
    trip = Trip.objects.all()
    context = {
        'trip': trip
    }
    return render(request, 'about_index.html', context)

