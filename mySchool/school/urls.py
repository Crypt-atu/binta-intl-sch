from django.urls import path
from school import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('contact/', views.contact, name = "contact"),
    path('courses/', views.Course, name='courses'),
    path('calendar/', views.SchoolCalendarView, name='school-calendar'),
    path('register/', views.Register, name="register"),

    #Path to the Login & Logout Views
    path('login/', auth_views.LoginView.as_view(template_name = 'Login.html'), name = 'login'),
    
    #Path for Authenticated Users
    path('home/', views.home, name="home"),
]