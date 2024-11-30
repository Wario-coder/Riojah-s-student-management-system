from django import forms
from.models import Students

class StudentForm (forms.ModelForm):
    class Meta:
        model = Students
        fields = ['student_number','First_name','Last_name','Email','Field_of_study','GPA']
        labels = {
     'student_number':'student Number',
        'First_name': 'First name',
        'Last_name': 'Last name',
        'Email':'Email',
        'Field_of_study':'Field of study',
        'GPA': 'GPA'

        }
        widgets = {
            'student_number': forms.NumberInput(attrs={'class': 'fare-control'}),
            'First_name': forms.TextInput(attrs={'class': 'fare-control'}),
            'Last_name': forms.TextInput(attrs={'class': 'fare-control'}),
            'Email': forms.EmailInput(attrs={'class': 'fare-control'}),
            'Field_of_study':forms.TextInput(attrs={'class': 'fare-control'}),
            'GPA':  forms.NumberInput(attrs={'class': 'fare-control'}),
        }

