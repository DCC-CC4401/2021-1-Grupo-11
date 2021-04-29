from django.shortcuts import render
from django.http import HttpResponseRedirect
from mainApp.models import Course, Department, Review, User, UserRoles, Roles
from django.contrib.auth import authenticate, login,logout


courses_Dict = {
    'DCC' : [('CC3001', 'CC3001 Algoritmos'), ('CC3002', 'CC3002 Gráfica'), ('CC5002', 'CC5002 Deep Learning')],
    'DIM' : [('MA1001', 'MA1001 Intro al álgebra'), ('MA2003', 'MA2003 Cálculo diferencial')],
    'DII' : [('IN3002', 'IN3002 Econo'), ('IN4002', 'IN3002 Evaluación de proyectos')]
}

# Create your views here.
def login_user(request):
    if request.method == 'GET':
        return render(request, "mainApp/login.html")  
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/index') # Pagina principal
        else:
            return HttpResponseRedirect('/login') # login

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login')

def register_user(request):
    if request.method == 'GET': 
        return render(request, "mainApp/register_user.html") 

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        # Create new user
        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        user.save()

        # Guardar rol de alumno
        role = Roles.objects.get(role_name='student')
        userRole = UserRoles(user=user, role=role) 
        userRole.save()
        
        # Redirect
        return HttpResponseRedirect('/login')

def register_review(request):
    if request.method == 'GET':
        #TODO: Pedir la info a la BD y mandarla al template
        # dict() -> html 
        context = dict()
        #roles = Roles.objects.filter(...)
        context['dict'] = courses_Dict
        return render(request, "mainApp/review_chanta.html", context)  #template de nombre review 

    elif request.method == 'POST':
        username = request.POST['username']
        user = User.objects.get(username=username) #este por ahora
        #user = request.user    """Este es el que queremos """

        course_string = request.POST['course']
        course = Course.objects.get(course_code=course_string)

        course = Course.objects.get()
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
        review = Review(user=user, course=course, section=section, year=year, semester=semester, required_time_level=required_time_level,
                        required_time_comment=required_time_comment, difficulty_level=difficulty_level, 
                        difficulty_comment=difficulty_comment, recommendation_level=recommendation_level, 
                        recommendation_comment=recommendation_comment, study_recommendation=study_recommendation,
                        extra_comment=extra_comment)
        review.save()

        #Redireccionar 
        return HttpResponseRedirect('/login')

"""
Para el proximo sprint (dropdow departamento filtra dropdown cursos)
def load_cursos(request):
    department_id = request.GET.get('department_id')
    courses = Courses.objects.filter(department_id = department_id).all() #retorna toda tupla en course tq department_id sea el recibido el post
    return render(request, '') #html con el dropdown de cursos
"""