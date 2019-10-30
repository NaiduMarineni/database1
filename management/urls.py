from django.urls import path
from . import views

urlpatterns = [
	path('students/', views.displaystudent, name='students'),
	path('home/', views.home, name='school-home'),
	path('addstudent/', views.studentCreate.as_view(), name='addstudent'),
	path('studentslist/', views.studentslist, name='studentslist'),
	path('searchstudent/', views.studentSearch, name ='searchstudent'),
	path('get_std_courses/(?P<studentId>\d+)/$', views.get_std_courses, name='get_std_courses'),
	#path('editstudent', views.studentUpdate, name='editstudent'),
	#path('deletestudent', views.studentDelete, name='deletestudent')
	path('departments/', views.departments, name='departments'),
	path('add_department/', views.departmentCreate.as_view(), name='add_department'),
	path('search_department/', views.departmentSearch, name='search_department'),
	path('departmentsList/', views.departmentsList, name='departmentsList'),

	path('staff/', views.staff_home, name='staff'),
	path('add_staff/', views.staffCreate.as_view(), name='add_staff'),
	path('search_staff/', views.staffSearch, name='search_staff'),
	path('staffList/', views.staffList, name='staffList'),
	path('edit_staff', views.staffUpdate.as_view(), name='update_staff'),

	path('courses/', views.courses_home, name='courses'),
	path('add_course/', views.courseCreate.as_view(), name='add_course'),
	path('search_course/', views.courseSearch, name='search_course'),
	path('courseList/', views.courseList, name='courseList'),
	path('edit_course/', views.courseUpdate.as_view(), name='edit_course'),

	path('get_course_stds/(?P<courseId>\w+)/$', views.get_course_stds, name='course_students'),
]

'''path('staff/', views.staff, name='staff'),
	path('add_staff/', views.staffCreate.as_view(), name='add_staff'),
	path('search_staff/', views.staffSearch, name='search_staff'),
	path('staffList/', views.departmentsList, name='staffList'),'''
