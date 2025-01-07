from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import StudentRegistrationForm, StudentLoginForm, EnrollmentForm, GuardianRegistrationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
#Index Page VIew
def index(request):
    department_num = Departments.objects.all().count()
    faculties_num = Faculties.objects.all().count()
    courses_num = Courses.objects.all().count()
    lecturers_num = Lecturers.objects.all().count()

    context = {'department_num': department_num,
                    'faculties_num': faculties_num,
                    'courses_num': courses_num,
                    'lecturers_num': lecturers_num}
    return render(request, 'index.html', context)

#Contact Page VIew
def contact(request):
    return render(request, 'contact.html')

#Course Page VIew
def Course(request):
    courses = Courses.objects.all()
    context = {'courses':courses}
    return render(request, 'Courses.html', context)

#Calendar Page VIew
def SchoolCalendarView(request):
    calendars = SchoolCalendar.objects.all()
    context = {'calendars':calendars}
    return render(request, 'calender-page.html', context)

#Register Page VIew
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

#Student Login View
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

#logout Page VIew
@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')

#Home Page VIew
@login_required(login_url='login')
def home(request):
    student = Students.objects.get(email=request.user.email)
    courses = student.courses.all()
    context = {'courses':courses}
    return render(request, 'home.html', context)

#Enrollment Page VIew
@login_required(login_url='login')
def enrollment(request):
    if request.method == "POST":
        form = EnrollmentForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EnrollmentForm(instance=request.user)
    return render(request, 'enrollment.html', {'form':form})

#Courses Detail View
class CourseDetailView(DetailView):
    model = Courses
    template_name = "detail_courses.html"

# Faculties and Departmental View
def fac_dep(request):
    faculties = Faculties.objects.all()  # Get all faculties

    # Build a dictionary mapping each faculty to its departments
    faculties_with_departments = {
        faculty: faculty.departments.all() for faculty in faculties
    }

    context = {
        'faculties': faculties_with_departments
    }
    return render(request, 'faculty_department.html', context)

#Department Detail View
class DepartmentDetailView(DetailView):
    model = Departments
    template_name = 'details_departments.html'

      # Override the get_context_data method to add lecturers
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the department object from the context
        department = self.get_object()
        
        # Filter lecturers based on the department
        lecturers = department.lectures.all()
        
        # Add the lecturers to the context
        context['lecturers'] = lecturers
        return context

#Faculties Detail View
class FacultyDetailView(DetailView):
    model = Faculties
    template_name = 'details_faculties.html'


#Result View
@login_required(login_url='login')
def Result(request):
    student = Students.objects.get(email=request.user.email)
    results = Results.objects.filter(student = student)

    context = {
               'results':results}
    return render(request, 'results.html', context)

#Guadians Create Views
class GuardianCreateView(LoginRequiredMixin, CreateView):
    model = Guardians
    form_class = GuardianRegistrationForm
    template_name = "guardians.html"
    success_url = 'home'
    login_url = 'login'
    

    def form_valid(self, form):
        form.instance.student = self.request.user  # Associate the guardian with the current user
        return super().form_valid(form)


