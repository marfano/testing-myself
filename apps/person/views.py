from django.http import JsonResponse
from django.views.generic import DeleteView, UpdateView, CreateView

from .forms import StudentForm, TeacherForm
from apps.schedule.models import Schedule
from .models import Student, Teacher

"""
'Django’s generic views were developed to ease that pain. 
They take certain common idioms and patterns found in view development 
and abstract them so that you can quickly write common views of data 
without having to write too much code.' - Django Project
>> I want to know more! I should visit: https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-display/
"""


"""General functions"""
# The function HttpResponse.is_ajax is deprecated. 
# I wrote mine.
def is_ajax(request):
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'

"""Student views"""

# Create a new student
class StudentCreate(CreateView):
	model = Student
	fields = ('__all__')
	template_name = 'student/student_create.html'
	success_url = 'student_create'

	def get_context_data(self, **kwargs): 
		# rewriting the get_context_data method of generic Django views
		context = super().get_context_data(**kwargs)
		context["students"] = Student.objects.all()
		context["schedule"] = Schedule.objects.all()
		return context

	# Rewrite the render to response function 
	# to more list-data-handler flexibility on html page
	def render_to_response(self, context, **response_kwargs):
		""" 
		A js object is a json
		a python dictionary is an object
		I should return a python dict (to handle the information better)
		to get it, i should transform the Httpresponse
		with JsonResponse module
		"""
		if is_ajax(self.request):
			# print('Es una petición ajax*********')
			data = list(context["students"].values())   # get the context calculated in get_context_data (queryset)
														# Transform Queryset -> array
			return JsonResponse({'students': data})     # and array -> to dictionary
		else:
			response_kwargs.setdefault('content_type', self.content_type)
			return self.response_class(
				request=self.request,
				template=self.get_template_names(),
				context=context,
				using=self.template_engine,
				**response_kwargs
			)


# Class view to update students
class StudentUpdate(UpdateView):
	model = Student
	form_class = StudentForm
	template_name = 'student/student_update.html'
	success_url = 'student_create'

# # Class view to delete students
class StudentDelete(DeleteView):
	model = Student
	template_name='student/student_confirm_delete.html'
	success_url = 'student_create'



"""Teacher views"""

# Create a new teacher
class TeacherCreate(CreateView):
	model = Teacher
	fields = ('__all__')
	template_name = 'teacher/teacher_create.html'
	success_url = 'teacher_create'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["teachers"] = Teacher.objects.all()
		return context


	# Rewrite the render to response function 
	# to more list-data-handler flexibility on html page
	def render_to_response(self, context, **response_kwargs):
		""" 
		A js object is a json
		a python dictionary is an object
		I should return a python dict (to handle the information better)
		to get it, i should transform the Httpresponse
		with JsonResponse module
		
		"""
		if is_ajax(self.request):
			# print('It's an ajax request*********')
			data = list(context["teachers"].values())   # get the context calculated in get_context_data (queryset)
														# Transform Queryset -> array
			return JsonResponse({'teachers': data})     # and array -> to dictionary
		else:
			response_kwargs.setdefault('content_type', self.content_type)
			return self.response_class(
				request=self.request,
				template=self.get_template_names(),
				context=context,
				using=self.template_engine,
				**response_kwargs
			)

# # Class view to update teachers
class TeacherUpdate(UpdateView):
	model = Teacher
	form_class = TeacherForm
	template_name = 'teacher/teacher_update.html'
	success_url = 'teacher_create'

# Class view to delete teachers
class TeacherDelete(DeleteView):
	model = Teacher
	template_name='teacher/teacher_confirm_delete.html'
	success_url = 'teacher_create'

