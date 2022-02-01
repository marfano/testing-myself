from django.urls import path
from django.views.generic import TemplateView
from apps.person.views import *

urlpatterns = [
    ## Index path
    path('', index),
  
    ## Student paths
    path('student_create/', StudentCreate.as_view(), name='student_create'),
    path('student_list/', StudentList.as_view(), name='student_list'),
    
    ## Teacher paths
    
]
