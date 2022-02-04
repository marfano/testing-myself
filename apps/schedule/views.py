from django.views.generic import CreateView, DeleteView

from .models import Schedule

"""
'Django’s generic views were developed to ease that pain. 
They take certain common idioms and patterns found in view development 
and abstract them so that you can quickly write common views of data 
without having to write too much code.' - Django Project
>> I want to know more! I should visit: https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-display/
"""

# Create your views here.

"""Schedule views"""

# Create a new schedule
class ScheduleCreate(CreateView):
	model = Schedule
	fields = ('__all__')
	template_name = 'schedule/schedule_create.html'
	success_url = '/schedule/schedule_create'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["schedules"] = Schedule.objects.all()
		return context

# Class view to delete schedules
class ScheduleDelete(DeleteView):
	model = Schedule
	template_name='schedule/schedule_confirm_delete.html'
	success_url = '/schedule/schedule_create'


