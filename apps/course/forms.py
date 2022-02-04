from django import forms
from apps.schedule.models import Schedule

class ScheduleForm(forms.ModelForm):
    model = Schedule
    schedule_options = forms.ModelMultipleChoiceField(queryset=Schedule.objects.all(), widget=forms.CheckboxSelectMultiple(), required=False)