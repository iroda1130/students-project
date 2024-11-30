from django.http import HttpResponse
from django.shortcuts import render
from .models import students, Student


def student_list(request):
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')
    email = request.GET.get('email')
    age = request.GET.get('age')
    if title is not None and content is not None:
        Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            age=age
        )
    students = Student.objects.all()
    ctx = {'students': students}
    return render(request, 'students/students_list.html', ctx)



