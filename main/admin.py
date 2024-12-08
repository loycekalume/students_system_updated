# from django.contrib import admin
# from .models import Student  # Replace with your model name
#
from django.contrib import admin
admin.site.site_header = 'StudentMS Administration'
admin.site.site_title = 'StudentMS Admin'

from main.models import Student, Course, Enrollment


class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','gender','dob']
    search_fields = ['first_name','last_name','email']
    list_filter = ['gender']
    list_title_page = 30


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','code','instructor','start_date','end_date']
    search_fields = ['name','code','instructor']
    list_filter = ['name']
    list_title_page = 5

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['student','course','enrollment_date','status']
    search_fields = ['student','course','status']
    list_filter = ['student']
    list_title_page = 30

admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)