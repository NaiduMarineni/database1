from django.urls import path
from . import views

urlpatterns = [
	path('students/', views.displaystudent, name='students'),
	path('home/', views.home, name='school-home'),
	path('addstudent/', views.studentCreate.as_view(), name='addstudent'),
	path('studentslist/', views.studentslist, name='studentslist')
]