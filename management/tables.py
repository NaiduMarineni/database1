import django_tables2 as tables 
from .models import student

class studentTable(tables.Table):
	class Meta:
		model = student
		template_name = "django_tables2/bootstrap.html"
		fields = ("name", "studentId")