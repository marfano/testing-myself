from django.urls import path
from apps.schedule.views import *

app_name='schedule'

urlpatterns = [
   
    path('schedule_create/', ScheduleCreate.as_view(), name='schedule_create'),
    path('schedule_delete/<int:pk>', ScheduleDelete.as_view(), name='schedule_delete'),

]