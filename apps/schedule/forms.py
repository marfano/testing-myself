from django import forms
from apps.schedule.models import Schedule

class ScheduleForm(forms.ModelForm):
    """ Form to register a Schedule

    """

    class Meta:
        model = Schedule

        fields = {
            'day',
            'hour',

        }

        labels = {
            'day': 'Dia',
            'hour': 'Hora',

        } 

        widgets = {
            'day': forms.Select(attrs={'class':'form-control'}),
            'hour': forms.Select(attrs={'class':'form-control'}),
        }

