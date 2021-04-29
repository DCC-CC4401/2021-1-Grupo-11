from django.db import models
from django.contrib.auth.models import AbstractUser
import django.utils.timezone

# Create your models here.
class User(AbstractUser):
	pass

class Roles(models.Model):
	role_name = models.CharField(max_length=255) #student / admin

class UserRoles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    role = models.ForeignKey(Roles, on_delete=models.CASCADE) 
    
class Course(models.Model):
	name = models.CharField(max_length=255) #ej Metodologias de Disenno y Programacion
	course_code = models.CharField(max_length=255) #ej CC3002
	course_type = models.CharField(max_length=255) #ej electivo

class Department(models.Model):
    name = models.CharField(max_length=255) #ej Depto Ing Electrica

class BelongsTo(models.Model):
	department = models.ForeignKey(Department, on_delete=models.CASCADE) 
	course = models.ForeignKey(Course, on_delete=models.CASCADE)  
	
class Review(models.Model):
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE) 
	timestamp = models.DateField(default=django.utils.timezone.now)
	
	# Versión del curso
	section = models.IntegerField()
	year = models.IntegerField()
	semester = models.IntegerField()
	
	# Respuestas
	required_time_level = models.IntegerField()
	required_time_comment = models.CharField(max_length=255)
	difficulty_level = models.IntegerField()
	difficulty_comment = models.CharField(max_length=255)
	recommendation_level = models.IntegerField()
	recommendation_comment = models.CharField(max_length=255)
	study_recommendation = models.CharField(max_length=255)
	extra_comment = models.CharField(max_length=255)

class UsefulFor(models.Model):
	review = models.ForeignKey(Review, on_delete=models.CASCADE) 
	course = models.ForeignKey(Course, on_delete=models.CASCADE)