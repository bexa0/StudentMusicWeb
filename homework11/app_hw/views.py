from django.shortcuts import render, redirect
from app_hw.models import *


def start_page_view(request):
    context = {'student_list': Students.objects.all()}

    return render(request, 'main_index.html', context)


def detail_student_view(request, student_slug):
    students_slug = Students.objects.get(slug=student_slug)
    context = {'students_slug': students_slug}

    return render(request, 'detail_student.html', context)


def create_student_view(request):
    context = {'instrument_list': MusicalInstrument.objects.all()}

    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        age = request.POST.get('age')
        course = request.POST.get('course')
        instrument = request.POST.get('instrument')
        grade = request.POST.get('grade')
        payment = request.POST.get('payment')

        student = Students()
        student.name = name
        student.surname = surname
        student.age = age
        student.course = course
        student.instrument = MusicalInstrument.objects.filter(pk=instrument)
        student.grade = grade
        student.payment = True if payment in request.POST else False
        student.save()

        return redirect('main_page')

    return render(request, 'create_student.html', context)