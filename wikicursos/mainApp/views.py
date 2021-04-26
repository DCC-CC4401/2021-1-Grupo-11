from django.shortcuts import render
from django.http import HttpResponseRedirect
from mainApp.models import Department, Review

# Create your views here.
def register_department(request):
    if request.method == 'GET': 
        return render(request, "mainApp/register_department.html")  #template de nombre new_department

    elif request.method == 'POST':
        name = request.POST['name']
        prefix = request.POST['prefix']
        
        #Crear la nueva review
        department = Department(name=name, prefix=prefix)
        department.save()

        #Redireccionar
        return HttpResponseRedirect('/register_department')

def register_course(request):
    if request.method == 'GET': 
        return render(request, "mainApp/register_course.html")  #template de nombre new_department

    elif request.method == 'POST':
        code = request.POST['code']
        name = request.POST['name']
        key = request.POST['key']
        ype = request.POST['ype']
        
        #Crear la nueva review
        course = Course(code=code, name=name, key=key, ype=ype)
        course.save()

        #Redireccionar
        return HttpResponseRedirect('/register_course')

def register_review(request):
    if request.method == 'GET': 
        return render(request, "mainApp/register_review.html")  #template de nombre review 

    elif request.method == 'POST':
        section = request.POST['section']
        year = request.POST['year']
        semester = request.POST['semester']
        required_time_level = request.POST['required_time_level']
        required_time_comment = request.POST['required_time_comment']
        difficulty_level = request.POST['difficulty_level']
        difficulty_comment = request.POST['difficulty_comment']
        recommendation_level = request.POST['recommendation_level']
        recommendation_comment = request.POST['recommendation_comment']
        study_recommendation = request.POST['study_recommendation']
        extra_comment = request.POST['extra_comment']

        #Crear la nueva review
        review = Review(section = section, year = year, semester = semester, required_time_level = required_time_level, required_time_comment = required_time_comment, difficulty_level = difficulty_level,  difficulty_comment = difficulty_comment, recommendation_level =recommendation_level, recommendation_comment = recommendation_comment, study_recommendation = study_recommendation, extra_comment = extra_comment)
        review.save()

        #Redireccionar 
        return HttpResponseRedirect('/inicio')

	