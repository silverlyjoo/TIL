from django.shortcuts import render, redirect
from .models import Student 

# Create your views here.

def index(request):
    students = Student.objects.all()
    return render(request, 'workshopapp/index.html', {'students':students})
    
def new(request):
    return render(request, 'workshopapp/new.html')
    
def create(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    birth = request.POST.get('birth')
    age = request.POST.get('age')
    student = Student(name=name, email=email, birthday=birth, age=age)
    student.save()
    return redirect('index')
    
def delete(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect('index')
    
def edit(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'workshopapp/edit.html', {'student':student})
    
def update(request, pk):
    student = Student.objects.get(pk=pk)
    student.name = request.POST.get('name')
    student.email = request.POST.get('email')
    student.birthday = request.POST.get('birth')
    student.age = request.POST.get('age')
    student.save()
    return redirect('index')
    