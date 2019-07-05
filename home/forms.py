from django import forms
from .models import Student

class StudentEditModelForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__' 
        # student_name, department
        widgets={
            'student_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Student Name'}),
            'department':forms.Select(attrs={'class':'custom-select'})
        }
class StudentSearchForm(forms.Form):
    q=forms.CharField(label='',
    widget=forms.TextInput(attrs={'class':'form-control','maxlength':'30',
    'placeholder':'Search'}))

class StudentCreateForm(forms.Form):
    student_name=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','maxlength':'50','placeholder':'Student Name'}))
    dept=(('CSE','Computer Science'),('MH','Mech'),('CV','Civil'))
    department=forms.CharField(label='',widget=forms.Select(attrs={'class':'form-control'},choices=dept))    