from django.db import models

# Create your models here.
class student(models.Model):
	name =  models.CharField(max_length = 100)
	studentId = models.BigIntegerField(primary_key = True)

	def __str__ (self):
		return self.name