from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def Course(request):
    courses = Courses.objects.all()
    context = {'courses':courses}
    return render(request, 'Courses.html', context)

def SchoolCalendarView(request):
    calendars = SchoolCalendar.objects.all()
    context = {'calendars':calendars}
    return render(request, 'calender-page.html', context)

def Register(request):
    return render(request, 'registration.html')


def home(request):
    return render(request, 'home.html')