from django.urls import path
from apps.course.views import *

app_name='course'

urlpatterns = [
    # Course paths
    path('', FilterView.as_view(), name='course_list'),
    
]
