from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView, CreateView

from .forms import StudentForm
from .models import Student

# Create your views here.

def index(request):
    return render(request,'index.html')


# Class view to list students
class StudentList(ListView):
	model = Student
	template_name='student/student_list.html'
	# paginate_by =0


class StudentCreate(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/student_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["students"] = Student.objects.all()
        return context