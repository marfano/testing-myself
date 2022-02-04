from django.urls import path
from apps.person.views import *

app_name='person'

urlpatterns = [
  
    ## Student paths
    path('student_create/', StudentCreate.as_view(), name='student_create'),
    path('student_update/<int:pk>', StudentUpdate.as_view(), name='student_update'),
    path('student_delete/<int:pk>', StudentDelete.as_view(), name='student_delete'),
    
    ## Teacher paths
    path('teacher_create/', TeacherCreate.as_view(), name='teacher_create'),
    path('teacher_update/<int:pk>', TeacherUpdate.as_view(), name='teacher_update'),
    path('teacher_delete/<int:pk>', TeacherDelete.as_view(), name='teacher_delete'),
    
]