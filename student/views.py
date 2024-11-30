from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from.models import Students
from.forms import StudentForm
def index(request):
    return render(request,'index.html',{
        'students' : Students.objects.all()

    })
def view_student(request,id):
    student= Students.objects.get(pk=id)
    return HttpResponseRedirect[reverse('index')]
def add(request):
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      new_student_number = form.cleaned_data['student_number']
      new_first_name = form.cleaned_data['First_name']
      new_last_name = form.cleaned_data['Last_name']
      new_email = form.cleaned_data['Email']
      new_field_of_study = form.cleaned_data['Field_of_study']
      new_gpa = form.cleaned_data['GPA']

      new_student = Students(
        student_number=new_student_number,
        First_name=new_first_name,
        Last_name=new_last_name,
        Email=new_email,
        Field_of_study=new_field_of_study,
        GPA=new_gpa
      )
      new_student.save()
      return render(request, 'Add.html', {
        'form': StudentForm(),
        'success': True
      })
  else:
    form = StudentForm()
  return render(request, 'Add.html', {
    'form': StudentForm()
  })


def edit(request, id):
  if request.method == 'POST':
    student = Students.objects.get(pk=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
      form.save()
      return render(request, 'edit.html', {
        'form': form,
        'success': True
      })
  else:
    student = Students.objects.get(pk=id)
    form = StudentForm(instance=student)
  return render(request, 'edit.html', {
    'form': form
  })


def delete(request, id):
  if request.method == 'POST':
    student = Students.objects.get(pk=id)
    student.delete()
  return HttpResponseRedirect(reverse('index'))

