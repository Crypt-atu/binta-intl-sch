from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import StudentRegistrationForm, StudentLoginForm
from django.urls import reverse

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
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = StudentRegistrationForm()

    context = {'form':form}
    return render(request, 'registration.html', context)

def student_login(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            print(f"Attempting to authenticate user with email: {email}")  # Debugging line
            user = authenticate(request, email=email, password=password)
            if user is not None:
                print("User authenticated successfully!")  # Debugging line
                login(request, user)
                return redirect('home')
            else:
                print("Authentication failed!")  # Debugging line
                form.add_error(None, 'Invalid email or password')
    else:
        form = StudentLoginForm()

    return render(request, 'Login.html', {'form': form})



def home(request):
    return render(request, 'home.html')