from django.db import models

# Create your models here.
class student(models.Model):
	name =  models.CharField(max_length = 100)
	studentId = models.BigIntegerField(primary_key = True)
	dept = models.ForeignKey('department', null = False, on_delete = models.CASCADE)

	#def __str__ (self):
		#return self.name

class staff(models.Model):
	name = models.CharField(max_length = 100)
	staffId = models.BigIntegerField(primary_key = True)
	dept = models.ForeignKey('department', on_delete = models.CASCADE)

	def __str__ (self):
		return str(self.staffId)

class department(models.Model):
	name = models.CharField(max_length = 100)
	dept_code = models.CharField(primary_key = True, max_length = 10)
	dept_head = models.ForeignKey('staff', null = True, on_delete = models.SET_NULL)

	def __str__ (self):
		return self.dept_code

class course(models.Model):
	course_name = models.CharField(max_length = 100)
	courseId = models.CharField(max_length = 10, primary_key = True)
	instructor = models.ForeignKey('staff', null = True, on_delete  = models.SET_NULL)

	def __str__ (self):
		return self.courseId

class grade(models.Model):
	student = models.ForeignKey('student', on_delete = models.CASCADE)
	course = models.ForeignKey('course', on_delete = models.CASCADE)
	gpa = models.IntegerField()

	class Meta:
		unique_together = (("student", "course"),)