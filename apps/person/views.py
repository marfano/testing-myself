from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView, CreateView

from .forms import StudentForm, TeacherForm
from .models import Student, Teacher

# Create your views here.


"""General views"""
def index(request):
    return render(request,'index.html')

"""Student views"""
# Class view to list students
class StudentList(ListView):
	model = Student
	template_name='student/student_list.html'
	# paginate_by =0

# Create a new student
class StudentCreate(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/student_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["students"] = Student.objects.all()
        return context


"""Teacher views"""
# Class view to list teachers
class TeacherList(ListView):
	model = Teacher
	template_name='teacher/teacher_list.html'
	# paginate_by =0

# Create a new teacher
class TeacherCreate(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teacher/teacher_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teacher"] = Teacher.objects.all()
        return context