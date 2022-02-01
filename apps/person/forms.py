from django import forms

from apps.person.models import Student, Teacher

class StudentForm(forms.ModelForm):
    """ Form to register a Student

    """

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
            # 'disponibility': forms.ModelMultipleChoiceField(queryset=Schedule.objects.all())
        }


class TeacherForm(forms.ModelForm):
    """ Form to register a Teacher

    """

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
            # 'disponibility': forms.ModelMultipleChoiceField(queryset=Schedule.objects.all())
        }