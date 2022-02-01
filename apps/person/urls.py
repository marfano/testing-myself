from django.urls import path
from apps.person.views import *

urlpatterns = [
    ## Index path
    path('', index),
  
    ## Student paths
    path('student_create/', StudentCreate.as_view(), name='student_create'),
    path('student_list/', StudentList.as_view(), name='student_list'),
    
    ## Teacher paths
    path('teacher_create/', TeacherCreate.as_view(), name='teacher_create'),
    path('teacher_list/', TeacherList.as_view(), name='teacher_list'),
    
]
