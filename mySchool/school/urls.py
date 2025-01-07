from django.urls import path
from school import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #Path for Authenticated Users
    path('home/', views.home, name="home"),
    path('enroll/', views.enrollment, name='enrollment'),
    path('result/', views.Result, name='result'),
    path('guardians', views.GuardianCreateView.as_view(), name='guardian'),
    
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

    #Reset Password Url
     path('password-reset/', auth_views.PasswordResetView.as_view(
         template_name="password_reset_form.html"
     ), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name="password_reset_done.html"
    ), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
    template_name="password_reset_confirm.html"
    ), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name="password_reset_complete.html"
    ), name='password_reset_complete'),

    #Path to the Login & Logout Views
    path('login/', views.student_login, name = 'login'),
    path('logout/', views.logout_view, name='logout'),
    
    
]