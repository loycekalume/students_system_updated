"""
URL configuration for students_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from main import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('students', views.students, name='students'),
path('add/student', views.add_student, name='add_student'),
    path('students/update/<int:student_id>', views.update_student, name='update_student'),
    path('students/delete/<int:student_id>', views.delete_student, name='delete_student'),
    path('courses', views.courses, name='courses'),
    path('courses/add/', views.add_course, name='add_course'),
    path('courses/<int:course_id>/edit/', views.edit_course, name='edit_course'),
    path('courses/<int:course_id>/delete/', views.delete_course, name='delete_course'),
    path('enrollments', views.enrollments, name='enrollments'),
    path('enrollments/add/', views.add_enrollment, name='add_enrollment'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_page, name='logout'),

    path('admin/', admin.site.urls),

]
