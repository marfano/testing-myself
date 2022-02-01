import pytest
import factory

from apps.person.models import Student, Teacher
from apps.schedule.models import Schedule

class StudentFactory(factory.Factory):  
    class Meta:
        model = Student

    email = 'john.snow@stark.com'
    name = 'John'
    last_name = 'Snow'
    modality = 'Grupal'
    level = 'Intermediate'


class TeacherFactory(factory.Factory):  
    class Meta:
        model = Teacher

    email = 'master.yoda@gimmerstick.com'
    name = 'Master'
    last_name = 'Yoda'


class ScheduleFactory(factory.Factory):  
    class Meta:
        model = Schedule

    day = 'Lunes'
    hour = '9.00'