from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import message
from django.shortcuts import render, get_object_or_404, redirect

from main.app_form import EnrollmentForm, CourseForm, StudentForm
from main.models import Student, Course, Enrollment


# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def students(request):
    students = Student.objects.all().order_by('-id').values()  # select * from students
    return render(request, 'students.html', {"students": students})


@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Student {form.cleaned_data['first_name']} was added!")
            return redirect('students')
    form = StudentForm()
    return render(request, 'student_form.html', {'form': form})


@login_required
def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect("students")


@login_required
def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, f"Student {form.cleaned_data['first_name']} was updated!")
            return redirect('students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_update_form.html', {"form": form})


@login_required
def courses(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})


@login_required
def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Course added successfully!")
            return redirect('courses')
    else:
        form = CourseForm()
    return render(request, 'course_form.html', {'form': form})


@login_required
# Edit an existing course
def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, f"Course '{course.name}' updated successfully!")
            return redirect('courses')
    else:
        form = CourseForm(instance=course)
    return render(request, 'course_edit_form.html', {'form': form})


@login_required
# Delete a course
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    course.delete()
    messages.success(request, f"Course '{course.name}' deleted successfully!")
    return redirect('courses')


@login_required
def enrollments(request):
    enrollments = Enrollment.objects.all()
    return render(request, 'enrollments.html', {'enrollments': enrollments})


@login_required
def add_enrollment(request):
    if request.method == "POST":
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Enrollment added successfully!")
            return redirect('enrollments')  # Ensure this URL is defined
    else:
        form = EnrollmentForm()
    return render(request, 'enrollment_form.html', {'form': form})


@login_required
def edit_enrollment(request, enrollment_id):
    enrollment = get_object_or_404(Enrollment, id=enrollment_id)
    if request.method == "POST":
        form = EnrollmentForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            messages.success(request, "Enrollment updated successfully!")
            return redirect('enrollments')
    else:
        form = EnrollmentForm(instance=enrollment)
    return render(request, 'enrollment_update_form.html', {'form': form, 'enrollment': enrollment})


def login_page(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'You are logged in')
            return redirect('dashboard')
        messages.warning(request, 'Invalid username or password')
        return redirect('login')


@login_required
def logout_page(request):
    logout(request)
    return redirect('login')
