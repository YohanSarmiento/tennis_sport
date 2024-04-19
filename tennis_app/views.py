from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

# Create your views here.

def home(request):
    return render(request, 'home.html')

def view_about(request):
    return render(request, 'about.html')


def tournaments(request):
    tournaments = Tournament.objects.all()  # Assuming Tournament is your model for tournaments
    context = {'tournaments': tournaments}
    return render(request, 'tournaments.html', context)

def venues(request):
    venues = Venue.objects.all()  # Assuming Tournament is your model for tournaments
    context = {'venues': venues}
    return render(request, 'venues.html', context)

def view_courses(request):
    courses = Course.objects.all()  # Assuming Course is your model for courses
    context = {'courses': courses}
    return render(request, 'courses.html', context)

def contact(request):
    return render(request, 'contact.html')