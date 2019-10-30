import django_tables2 as tables 
from .models import student, department, staff, course

class studentTable(tables.Table):
	class Meta:
		model = student
		template_name = "django_tables2/bootstrap.html"
		fields = ("name", "studentId")

class departmentTable(tables.Table):
	class Meta:
		model = department
		template_name = "django_tables2/bootstrap.html"
		fields = ("name", "dept_code", "dept_head")

class staffTable(tables.Table):
	class Meta:
		model = staff
		template_name = "django_tables2/bootstrap.html"
		fields = ("name", "staffId", "dept")

class courseTable(tables.Table):
	class Meta:
		model = course
		template_name = "django_tables2/bootstrap.html"
		fields = ("name", "courseId", "instructor")
