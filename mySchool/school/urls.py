from django.urls import path
from school import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('contact/', views.contact, name = "contact"),
    path('courses/', views.Course, name='courses'),
    path('calendar/', views.SchoolCalendarView, name='school-calendar'),
]