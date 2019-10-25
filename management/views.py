from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
# Create your views here.
from django.http import HttpResponse
from django_tables2 import SingleTableView
from .tables import studentTable
from management.models import student
from django.forms import ModelForm
from django.urls import reverse, reverse_lazy

data = student.objects.all()

class studentListView(SingleTableView):
	model = student
	table_class = studentTable
	template_name = 'management/student.html'

class studentCreate(CreateView):
	model = student
	fields = ['name', 'studentId']
	success_url = reverse_lazy('students')

class studentUpdate(UpdateView):
	model = student
	fields = ['name', 'studentId']
	template_name_suffix = '_update_form'
	success_url = reverse_lazy('students')

def searchStudent(request):
	context {
		'studentId' : 
		'student name ' : 
	}

def home(request):
	#print('I am here')
	
	context = {
		'table' : data
	}
	return render(request, 'management/home.html', context)	

def displaystudent(request):
	#RequestConfig(request).configure(table)
	return render(request, 'management/student.html',)

def studentslist(request):
	context = {
		'table' : student.objects.all()
	}
	print('I am here')
	print(data)
	#RequestConfig(request).configure(table)
	return render(request, 'management/studentslist.html', context)