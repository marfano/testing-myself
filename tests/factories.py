import pytest
import factory

from apps.person.models import Student, Teacher

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