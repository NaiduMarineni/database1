from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    studentId = forms.IntegerField(label='StudentId')
