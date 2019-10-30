from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
# Create your views here.
from django.http import HttpResponse
from django_tables2 import SingleTableView
from .tables import studentTable, departmentTable, staffTable, courseTable
from management.models import student, department, staff, course, grade
from django.forms import ModelForm
from django.urls import reverse, reverse_lazy
from django.template import RequestContext
from .forms import StudentForm 
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django import forms

from django.core.paginator import Paginator

class RawPaginator(Paginator):
    def __init__(self, object_list, per_page, count, **kwargs):
        super().__init__(object_list, per_page, **kwargs)
        self.raw_count = count

    def _get_count(self):
        return self.raw_count
    count = property(_get_count)

    def page(self, number):
        number = self.validate_number(number)
        return self._get_page(self.object_list, number, self)

def home(request):
	#print('I am here')
	return render(request, 'management/home.html',)	


class studentListView(SingleTableView):
	model = student
	table_class = studentTable
	template_name = 'management/student.html'

class studentCreate(CreateView):
	model = student
	fields = ['name', 'studentId', 'dept']
	success_url = reverse_lazy('students')

class studentUpdate(UpdateView):
	model = student
	fields = ['name', 'studentId']
	template_name_suffix = '_update_form'
	success_url = reverse_lazy('students')

def displaystudent(request):
	#RequestConfig(request).configure(table)
	return render(request, 'management/student.html',)

def get_std_courses(request, studentId):
	search_rslt = grade.objects.raw('SELECT * FROM management_grade mg WHERE mg.student_id = %s', [studentId])
	std_dtls = student.objects.raw('SELECT * FROM management_student ms WHERE ms.studentId = %s', [studentId])
	return render(request, 'management/student_grades.html', { 'grades': search_rslt, 'std_dtls' : std_dtls})

def studentslist(request):
	print("I am here")
	if request.method == 'POST' :
		request.session['DepartmentFilter'] = request.POST.get('DepartmentFilter')
	
	if request.session.get('DepartmentFilter') == None:
		user_list = student.objects.all()
	elif request.session.get('DepartmentFilter') == 'ALL':
		user_list = student.objects.all()
	else:
		user_list = student.objects.filter(dept = request.session.get('DepartmentFilter'))

	page = request.GET.get('page', 1)

	depts = department.objects.all()
	paginator = Paginator(user_list, 20)
	try:
	    users = paginator.page(page)
	except PageNotAnInteger:
	    users = paginator.page(1)
	except EmptyPage:
		users = paginator.page(paginator.num_pages)
	
	return render(request, 'management/studentslist.html', { 'users': users, 'depts' : depts})

class searchForm(forms.Form):
    studentId = forms.IntegerField()
def studentSearch(request):
	# if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        id = request.POST.get('studentId')
        search_rslt = student.objects.raw('SELECT * FROM management_student WHERE studentId = %s', [id])

        srch_form = searchForm()
        return render(request, 'management/student_search.html', {'rslt': search_rslt, 'form': srch_form})
        # check whether it's valid:
        #if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('')

    # if a GET (or any other method) we'll create a blank form
    else:
        srch_form = searchForm()
        return render(request, 'management/student_search.html', {'form': srch_form})

    return render(request, 'management/student_search.html', {'form': form})



def departments(request):
	return render(request, 'management/department.html',)

class departmentListView(SingleTableView):
	model = department
	table_class = departmentTable
	template_name = 'management/department.html'

class departmentCreate(CreateView):
	model = department
	fields = ['name', 'dept_code', 'dept_head']
	success_url = reverse_lazy('departments')

class departmentUpdate(UpdateView):
	model = department
	fields = ['dept_code', 'name', 'dept_head']
	template_name_suffix = '_update_form'
	success_url = reverse_lazy('departments')

def departmentSearch(request):
	return render(request, 'management/department.html',)

def departmentsList(request):
	return render(request, 'management/department.html',)


def staff_home(request):
	return render(request, 'management/staff.html',)

class staffListView(SingleTableView):
	model = staff
	table_class = staffTable
	template_name = 'management/staff.html'

class staffCreate(CreateView):
	model = staff
	fields = ['name', 'staffId', 'dept']
	success_url = reverse_lazy('staff')

class staffUpdate(UpdateView):
	model = staff
	fields = ['name', 'staffId', 'dept']
	template_name_suffix = '_update_form'
	success_url = reverse_lazy('staff')

def staffSearch(request):
	return render(request, 'management/staff.html',)

def staffList(request):
	return render(request, 'management/staff.html',)



def courses_home(request):
	return render(request, 'management/course.html',)

class courseListView(SingleTableView):
	model = course
	table_class = courseTable
	template_name = 'management/course.html'

class courseCreate(CreateView):
	model = course
	fields = ['course_name', 'courseId', 'instructor']
	success_url = reverse_lazy('courses')

class courseUpdate(UpdateView):
	model = course
	fields = ['course_name', 'courseId', 'instructor']
	template_name_suffix = 'course_update_form.html'
	success_url = reverse_lazy('courses')


class searchCourseForm(forms.Form):
    courseId = forms.CharField()

def courseSearch(request):
	srch_form = searchCourseForm()
	if request.method =='GET':
		crsId = request.GET.get('courseId')
		print(crsId)
		course_list = course.objects.raw('SELECT * FROM management_course mc JOIN management_staff ms ON \
			mc.instructor_id = ms.staffId WHERE mc.courseId = %s', [crsId,])
		return render(request, 'management/course_search.html', {'courses': course_list, 'form': srch_form} )

	else:
		return render(request, 'management/course_search.html', {'form': srch_form} )


def courseList(request):
	if request.method == 'POST' :
		request.session['DepartmentFilter'] = request.POST.get('DepartmentFilter')
	
	if request.session.get('DepartmentFilter') == None:
		request.session['DepartmentFilter'] = 'ALL'
		course_list = course.objects.raw('SELECT * FROM management_course mc JOIN management_staff ms ON \
			mc.instructor_id = ms.staffId ')
	elif request.session.get('DepartmentFilter') == 'ALL':
		course_list = course.objects.raw('SELECT * FROM management_course mc JOIN management_staff ms ON \
			mc.instructor_id = ms.staffId ')
	else:
		course_list = course.objects.raw('SELECT * FROM management_course mc JOIN management_staff ms ON \
			mc.instructor_id = ms.staffId WHERE ms.dept_id = %s', [request.session.get('DepartmentFilter')])

	#page = request.GET.get('page', 1)

	depts = department.objects.all()
	
	return render(request, 'management/courselist.html', { 'courses': course_list, 'depts' : depts})

def get_course_stds(request, courseId):
	search_rslt = grade.objects.raw('SELECT * FROM management_grade mg JOIN management_student ms ON \
		mg.student_id = ms.studentId WHERE mg.course_id = %s', [courseId])
	course_dtls = course.objects.raw('SELECT * FROM management_course mc JOIN management_staff ms ON \
			mc.instructor_id = ms.staffId WHERE mc.courseId = %s', [courseId])
	return render(request, 'management/course_students.html', {'students' : search_rslt, 'course': course_dtls })


