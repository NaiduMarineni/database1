import datetime
import random
from django.core.management.base import BaseCommand
from management.models import student, department, staff, course, grade


dept_codes = ['CSCE', 'ECE', 'MECH', 'CVE', 'AESP', 'CHE', 'MTH', 'PHY', 'ARTS', 'IDE']
dept_names = ['Computer Science & Eng', 'Electrical & Computer Eng', 'Mechanical Eng', 'Civil Eng',
             'Aerospace Eng', 'Chemical Eng', 'Mathematics', 'Physics', 'Arts', 'Industrial Eng']

def generate_dept():
    index = random.randint(0, 9)
    return dept_codes[index]

def generate_name():
    x = ''
    len = random.randint(7, 20)
    for i in range(len):
        x += chr(ord('a')+random.randint(0,25))
    return x

def generate_grade():
    x = random.randint(0, 10)
    if(x > 7):
        return 4
    elif (x > 4):
        return 3
    elif (x > 2):
        return 2
    elif (x > 0):
        return 1
    else:
        return 0

def generate_id():
    return random.randint(10000, 100000)

class Command(BaseCommand):
    def add_departments():
        for i in range(10):
            dept = department(dept_code=dept_codes[i], name=dept_names[i])
            dept.save()

    def add_students(count):
        i =0;
        f = open("../first_names.csv.txt", 'r')
        lines = f.readlines()
        stnames = [each.replace('\n','') for each in lines] 
        while i < count:
            stid = generate_id()
            stname = stnames[i]
            code = generate_dept()
            #print(code)
            stdept = department.objects.get(dept_code = code)
            #stdept = generate_dept()
            if student.objects.filter(studentId = stid).exists():
                continue;
            else:
                newentry = student(name = stname, studentId = stid)
                newentry.dept = stdept
                newentry.save()
                i += 1

    def add_staff(count):
        i = 0;
        f = open("../first_names.csv.txt", 'r')
        lines = f.readlines()
        stnames = [each.replace('\n','') for each in lines] 
        while i < count:
            stid = generate_id()
            stname = stnames[i+2000]
            code = generate_dept()
            #print(code)
            stdept = department.objects.get(dept_code = code)
            #stdept = generate_dept()
            if staff.objects.filter(staffId = stid).exists():
                continue;
            else:
                newentry = staff(name = stname, staffId = stid)
                newentry.dept = stdept
                newentry.save()
                i += 1

    def add_courses(count):
        i=0
        for dept in dept_codes:
            for i in range(count):
                crsId = dept+format(i+1, '03d')
                x = staff.objects.filter(dept = dept)
                instructor = x[random.randint(0, x.count()-1)]
                #dept_obj = department.objects.get(dept_code = dept)
                newentry = course(course_name = generate_name(), instructor = instructor, courseId = crsId)
                newentry.save()

    def add_grades():
        for each_st in student.objects.all():
            dept = each_st.dept
            instrs = staff.objects.filter(dept = dept)
            courses  = course.objects.filter(instructor__in = instrs)
            count = 0;
            size = len(courses)
            while count < 4:
                crs = courses[count]
                #crs = courses[random.randint(0, size-1)]
                #if grade.objects.filter(student = each_st, course = crs).exists:
                #   continue
                #else:
                newentry = grade(student = each_st, course = crs, gpa = generate_grade())
                newentry.save()
                count += 1

    def handle(self, *args, **kwargs):
        Command.add_departments()
        Command.add_students(1000)
        Command.add_staff(100)
        Command.add_courses(20)
        Command.add_grades()