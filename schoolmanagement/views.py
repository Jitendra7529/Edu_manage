from django.shortcuts import render, get_object_or_404, redirect
from django.http import request
from .models import Student, Teacher, Subject

# Create your views here.

def index(request):
    return render(request, 'index.html')

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})

def teacher_create(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        Teacher.objects.create(firstname=firstname, lastname=lastname)
        return redirect('teacher_list')
    return render(request, 'teacher_form.html')

def teacher_update(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    if request.method == 'POST':
        teacher.firstname = request.POST['firstname']
        teacher.lastname = request.POST['lastname']
        teacher.save()
        return redirect('teacher_list')
    return render(request, 'teacher_form.html', {'teacher': teacher})

def teacher_delete(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    teacher.delete()
    return redirect('teacher_list')

# Student views
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        Student.objects.create(firstname=firstname, lastname=lastname)
        return redirect('student_list')
    return render(request, 'student_form.html')

def student_update(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.firstname = request.POST['firstname']
        student.lastname = request.POST['lastname']
        student.save()
        return redirect('student_list')
    return render(request, 'student_form.html', {'student': student})

def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')

# Subject views
def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subject_list.html', {'subjects': subjects})

def subject_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        Subject.objects.create(name=name)
        return redirect('subject_list')
    return render(request, 'subject_form.html')

def subject_update(request, id):
    subject = get_object_or_404(Subject, id=id)
    if request.method == 'POST':
        subject.name = request.POST['name']
        subject.save()
        return redirect('subject_list')
    return render(request, 'subject_form.html', {'subject': subject})

def subject_delete(request, id):
    subject = get_object_or_404(Subject, id=id)
    subject.delete()
    return redirect('subject_list')

    