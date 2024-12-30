from django.urls import path
from school import views

urlpatterns = [
    #Path for Authenticated Users
    path('home/', views.home, name="home"),
    path('enroll/', views.enrollment, name='enrollment'),
    
    #Public Views
    path('index/', views.index, name='index'),
    path('contact/', views.contact, name = "contact"),
    path('courses/', views.Course, name='courses'),
    path('calendar/', views.SchoolCalendarView, name='school-calendar'),
    path('register/', views.Register, name="register"),
    path('detail/<int:pk>/', views.CourseDetailView.as_view(), name='detail'),
    path('detail-faculty/<int:pk>/', views.FacultyDetailView.as_view(), name='detail-faculty'),
    path('detail-department/<int:pk>/', views.DepartmentDetailView.as_view(), name='detail-department'),
    path('faculty_department/', views.fac_dep, name="fac_dep"),

    #Path to the Login & Logout Views
    path('login/', views.student_login, name = 'login'),
    path('logout/', views.logout_view, name='logout'),
    
    
]