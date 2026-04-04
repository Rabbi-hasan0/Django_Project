from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm
from django.http import HttpResponse
from .models import Student
from django.contrib import messages
# Create your views here.

def student_list(request):
    data=Student.objects.filter(is_deleted=False)
    return render(request, 'students/student_list.html', {'students': data})


def student_create(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student created successfully!')
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_create.html', {'form': form})


def student_update(request, pk):
    form = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully!')
            return redirect('student_list')
    else:
        form = StudentForm(instance=form)
    return render(request, 'students/student_update.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.is_deleted = True
        messages.success(request, 'Student deleted successfully!')
        student.save()
        return redirect('student_list')
    return render(request, 'students/student_delete.html', {'student': student})