from django.urls import path
from school import views

urlpatterns = [
    #Path for Authenticated Users
    path('home/', views.home, name="home"),
    
    path('index/', views.index, name='index'),
    path('contact/', views.contact, name = "contact"),
    path('courses/', views.Course, name='courses'),
    path('calendar/', views.SchoolCalendarView, name='school-calendar'),
    path('register/', views.Register, name="register"),

    #Path to the Login & Logout Views
    path('login/', views.student_login, name = 'login'),
    
    
]