from django.shortcuts import render

from main.models import Student, Course, Enrollment


# Create your views here.
def dashboard(request):
    return render(request,'dashboard.html')


def students(request):
    student = Student.objects.all().order_by('-id').values()  # select * from students
    return render(request, 'students.html', {"student": student})


def courses(request):
    course = Course.objects.all()
    return render(request, 'courses.html', {'course': course})



def enrollments(request):
    enrollment = Enrollment.objects.all()
    return render(request, 'enrollments.html', {'enrollment': enrollment})
