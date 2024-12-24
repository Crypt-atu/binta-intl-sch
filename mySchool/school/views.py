from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import StudentRegistrationForm, StudentLoginForm
from django.contrib.auth.decorators import login_required

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
            messages.error(request, "Your password can’t be too similar to your other personal information, Your password must contain at least 8 characters, Your password can’t be a commonly used password, Your password can’t be entirely numeric.")
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
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            messages.error(request, "Invalid Username or Password")        
    else:
        form = StudentLoginForm()

    return render(request, 'Login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')