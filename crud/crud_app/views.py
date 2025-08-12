from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Student
from .forms import StudentForm, RegisterForm

# Show list of students
def student_list(request):
    students = Student.objects.all().order_by('name')
    return render(request, 'student_list.html', {'students': students})

# Add a new student
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully.")
            return redirect('student_list')
    else:
        form = StudentForm()
    
    return render(request, 'student.html', {
        'form': form,
        'title': 'Add Student',
        'action_url': 'add_student'
    })

# Edit an existing student
def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully.")
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    
    return render(request, 'student.html', {
        'form': form,
        'title': 'Edit Student',
        'action_url': 'update_student',
        'id': id
    })

# Delete a student
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        messages.success(request, "Student deleted.")
        return redirect('student_list')
    return render(request, 'confirm_delete.html', {'student': student})

# Register a new admin user
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email is already registered.")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.is_staff = True
                user.is_superuser = True
                user.save()
                messages.success(request, "Admin user registered successfully.")
                return redirect('/admin/login/?next=/admin/')

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

