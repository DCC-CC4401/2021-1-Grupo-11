from django.shortcuts import render
from django.http import HttpResponseRedirect
from mainApp.models import Course, Department, Review, User, UserRoles, Roles, BelongsTo
from django.contrib.auth import authenticate, login, logout
import statistics as st


courses_Dict = {
    'DCC' : [('CC3001', 'CC3001 Algoritmos'), ('CC3002', 'CC3002 Gráfica'), ('CC5002', 'CC5002 Deep Learning')],
    'DIM' : [('MA1001', 'MA1001 Intro al álgebra'), ('MA2003', 'MA2003 Cálculo diferencial')],
    'DII' : [('IN3002', 'IN3002 Econo'), ('IN4002', 'IN3002 Evaluación de proyectos')]
}

lista_indicadores = ['required_time', 'difficulty', 'recommendation', 'practicality', 
        'content_adjustment', 'stress', 'teamwork', 'fondness', 'usefulness']

lista_comentarios = ['general', 'useful_courses', 'tools', 'study_recommendation']

title_dict = {
    'required_time': '¿El tiempo dedicado al ramo se ajusta a los créditos del curso?',
    'fondness': '¿Qué tanto te gustó la materia que viste?​',
    'difficulty': "¿Académicamente que tan difícil fue?",
    'recommendation': "¿Qué tanto recomiendas el curso?",
    'practicality': '¿Qué tan teórico práctico es el curso?',
    'content_adjustment': '¿Las evaluaciones están ajustadas al contenido visto en clase?',
    'stress': '¿Qué tanto estrés te generó el curso?',
    'teamwork': '¿Qué tanto trabajo en equipo requiere este curso?',
    'usefulness': '¿Crees que este curso será util en tu vida profesional?'
}

bounds_dict = {
    'required_time': ["Muy de acuerdo, me consumió mucho más tiempo", "Muy en desacuerdo, me consumió el tiempo señalado o menos"],
    'fondness': ["No me gustó nada", "Me gustó mucho"],
    'difficulty': ["Muy fácil", "Muy difícil"],
    'recommendation': ["Nada recomendable", "Muy recomendable"],
    'practicality': ['Totalmente teórico', 'Totalmente práctico'],
    'content_adjustment': ['Muy en desacuerdo, no tenían relación', 'Muy de acuerdo, estaban muy relacionadas'],
    'stress': ['Nada de estrés', 'Excesivo estrés'],
    'teamwork': ['Estríctamente individual', 'Estríctamente grupal'],
    'usefulness': ['Poco útil', 'Muy útil']
}
        

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, "mainApp/index.html")
    else:
        return HttpResponseRedirect('/login')


def login_user(request):
    if not request.user.is_authenticated:
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
    else:
        return HttpResponseRedirect('/index')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login')

def register_user(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return render(request, "mainApp/register_user.html") 
        else:
            return HttpResponseRedirect('/index')

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

        if request.user.is_authenticated:
            course_id = request.GET.get('course_id')
            course_name = Course.objects.filter(id=course_id).values('name')[0]['name']

            context = dict()
            #roles = Roles.objects.filter(...)
            context['dict'] = courses_Dict
            context['course_id'] = course_id
            context['course_name'] = course_name
            return render(request, "mainApp/formulario.html", context)  # template de nombre review 

        else:
            # If no user is logged in
            return HttpResponseRedirect('/login')

    elif request.method == 'POST':
        user = request.user    #usuario loggeado

        course_id = request.POST['course_id']
        course = Course.objects.get(id=course_id)

        section = request.POST['section']
        year = request.POST['year']
        semester = request.POST['semester']

        # Alternativas
        required_time_level = request.POST['required_time_level']
        required_time_comment = request.POST.get('required_time_comment', '')
        difficulty_level = request.POST['difficulty_level']
        difficulty_comment = request.POST.get('difficulty_comment', '')
        recommendation_level = request.POST['recommendation_level']
        recommendation_comment = request.POST.get('recommendation_comment', '')
        practicality_level = request.POST['practicality_level']
        practicality_comment = request.POST.get('practicality_comment', '')
        content_adjustment_level = request.POST['content_adjustment_level']
        content_adjustment_comment = request.POST.get('content_adjustment_comment', '')
        stress_level =  request.POST['stress_level']
        stress_comment = request.POST.get('stress_comment', '')
        teamwork_level = request.POST['teamwork_level']
        teamwork_comment = request.POST.get('teamwork_comment', '')
        fondness_level = request.POST['fondness_level']
        fondness_comment = request.POST.get('fondness_comment', '')
        usefulness_level = request.POST['usefulness_level']
        usefulness_comment = request.POST.get('usefulness_comment', '')

        # Texto
        study_recommendation_comment = request.POST.get('study_recommendation_comment', '')
        tools_comment = request.POST.get('tools_comment', '')
        useful_courses_comment = request.POST.get('useful_courses_comment', '')
        general_comment = request.POST.get('general_comment', '')

        #Crear la nueva review
        review = Review(user=user, course=course, section=section, year=year, semester=semester, required_time_level=required_time_level,
                        required_time_comment=required_time_comment, difficulty_level=difficulty_level, 
                        difficulty_comment=difficulty_comment, recommendation_level=recommendation_level, 
                        recommendation_comment=recommendation_comment, practicality_level = practicality_level,
                        practicality_comment = practicality_comment, content_adjustment_level = content_adjustment_level,
                        content_adjustment_comment = content_adjustment_comment, stress_level =  stress_level,
                        stress_comment = stress_comment, teamwork_level = teamwork_level, teamwork_comment = teamwork_comment,
                        fondness_level = fondness_level, fondness_comment = fondness_comment, usefulness_level = usefulness_level,
                        usefulness_comment = usefulness_comment, study_recommendation_comment = study_recommendation_comment,
                        tools_comment = tools_comment, useful_courses_comment = useful_courses_comment, 
                        general_comment = general_comment)
                         
        review.save()

        #Redireccionar 
        return HttpResponseRedirect(f'/gracias?course_id={course_id}')

"""
Para el proximo sprint (dropdown departamento filtra dropdown cursos)
def load_cursos(request):
    department_id = request.GET.get('department_id')
    courses = Courses.objects.filter(department_id = department_id).all() #retorna toda tupla en course tq department_id sea el recibido el post
    return render(request, '') #html con el dropdown de cursos
"""

def searchDepartment(request):
    if request.user.is_authenticated:
        context = {}
        dep_list = Department.objects.all()
        context['dep_list'] = dep_list
        return render(request, "mainApp/departamento.html", context)
    else:
        return HttpResponseRedirect('/login')

def searchCourse(request):
    if request.user.is_authenticated:
        context = {}
        dep_id = request.GET.get('dep')
        # ACA CONSULTA BASE DE DATOS
        courses_id_list = list(BelongsTo.objects.filter(department_id = dep_id).values('course_id'))
        courses_id_list = list(map(lambda x: x['course_id'], courses_id_list))

        courses_list = list(Course.objects.filter(id__in = courses_id_list).values('name', 'id'))

        context['dep_id'] = dep_id
        context['courses_id_list'] = courses_id_list
        context['courses_list'] = courses_list
        return render(request, "mainApp/curso.html", context)
    else:
        return HttpResponseRedirect('/login')


"""
Funcion que dada una lista de indicadores, retorna un string con el promedio y cuenta de puntajes
de cada indicador
"""
def statistics(request):

    def mean_count_aux(indicador, data_string, is_level=True):
        indicador_level = list(review_object_filter.values(indicador + '_level'))
        indicador_comment = list(review_object_filter.values(indicador + '_comment'))
        indicador_level = list(map(lambda x: x[indicador + '_level'], indicador_level))
        indicador_comment = list(filter(lambda x: x != '', list(map(lambda x: x[indicador + '_comment'], indicador_comment))))
        indicador_level_mean = st.mean(indicador_level)
        data_string += indicador +': {'
        data_string += 'title: ' + '"' +str(title_dict[indicador]) + '",'
        data_string += 'mean: ' + str(indicador_level_mean) + ','
        data_string += 'count: ' + str([indicador_level.count(i) for i in range(1, 6)]) +','
        data_string += 'comment: ' + str(indicador_comment) + ','
        data_string += 'bounds: ' + str(bounds_dict[indicador]) + ','
        data_string += '},'
        return data_string

    if request.user.is_authenticated:

        course_id = request.GET.get('course_id')
        course_name = Course.objects.filter(id=course_id).values('name')[0]['name']

        # ACA CONSULTA BASE DE DATOS
        review_object_filter = Review.objects.filter(course_id = course_id)
        
        count_review = review_object_filter.count()
        if count_review == 0:
            context = {'ErrorString' : 'No hay reviews para este curso',
                        'course_id' : course_id}
            return render(request, 'mainApp/reviewError.html', context)
        print(count_review)

        data_string = 'data={' 
        for indicador in lista_indicadores:
            data_string = mean_count_aux(indicador, data_string)
        data_string += '};' 


        comments_string = 'comments={'
        for comentario in lista_comentarios:
            comment_list = list(review_object_filter.values(comentario + '_comment'))
            comment_list = list(filter(lambda x: x != '', list(map(lambda x: x[comentario + '_comment'], comment_list))))
            comments_string += comentario + ':' + str(comment_list) + ','
            
        comments_string += '};' 

        

        context = {}
        context['listString'] = data_string
        context['countReview'] = "countReview="+str(count_review)+""
        context['course_id'] = course_id
        context['course_name'] = course_name
        context['commentsString'] = comments_string

        # renderear
        return render(request, "mainApp/statistics.html", context)

    else:
        return HttpResponseRedirect('/login')
        

def gracias(request):
    if request.user.is_authenticated:
        course_id = request.GET.get('course_id')
        context = {'course_id' : course_id}
        return render(request, "mainApp/gracias.html", context)
    else:
        return HttpResponseRedirect('/login')