from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	pass

class Roles(models.Model):
    role_name = models.CharField(max_length=255)

class UserRoles(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) 
    role_id = models.ForeignKey(Roles, on_delete=models.CASCADE) #constructor recibe un objeto de clase Roles
    
class Course(models.Model):
	code = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	key = models.CharField(max_length=255) #TODO: Revisar
	ype = models.CharField(max_length=255) #TODO: Revisar

class Department(models.Model):
    name = models.CharField(max_length=255)
    prefix = models.CharField(max_length=255)

class BelongsTo(models.Model):
	department_id = models.ForeignKey(Department, on_delete=models.CASCADE) 
	course_id = models.ForeignKey(Course, on_delete=models.CASCADE) 
	
class Review(models.Model):
	course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
	user_id = models.ForeignKey(User, on_delete=models.CASCADE) 
	timestamp = models.DateField(default=date.today())
	
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
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE) 
    usefulFor_id = models.IntegerField()
