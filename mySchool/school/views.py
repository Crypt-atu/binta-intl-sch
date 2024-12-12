from django.shortcuts import render
from .models import *

# Create your views here.
def course(request):
    courses = Courses.objects.all()
    context = {'courses':courses}
    return render(request, 'Courses.html', context)