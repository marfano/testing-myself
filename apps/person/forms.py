from django import forms

from apps.person.models import Student, Teacher
from apps.schedule.models import Schedule

class StudentForm(forms.ModelForm):
    """ Form to register a Student

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['disponibility'].queryset = Schedule.objects.all()

    class Meta:
        model = Student

        fields = {
            'email',
            'name',
            'last_name',
            'modality',
            'level',
            'disponibility'
        }

        labels = {
            'email': 'Email',
            'name': 'Nombre',
            'last_name': 'Apellido',
            'modality': 'Modalidad',
            'level': 'Nivel',
            'disponibility': 'Horarios'
        } 

        widgets = {
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'modality': forms.Select(attrs={'class':'form-control'}),
            'level': forms.Select(attrs={'class':'form-control'}),
            'disponibility': forms.SelectMultiple(attrs={'class':'form-control'})
        }


class TeacherForm(forms.ModelForm):
    """ Form to register a Teacher

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['disponibility'].queryset = Schedule.objects.all()

    class Meta:
        model = Teacher

        fields = {
            'email',
            'name',
            'last_name',
            'disponibility'
        }

        labels = {
            'email': 'Email',
            'name': 'Nombre',
            'last_name': 'Apellido',
            'disponibility': 'Horarios'
        } 

        widgets = {
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'disponibility': forms.SelectMultiple(attrs={'class':'form-control'})
        }