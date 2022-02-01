import factory
import pytest

from apps.person.models import Student

class StudentFactory(factory.Factory):  
    class Meta:
        model = Student

    email = 'john.snow@stark.com'
    name = 'John'
    last_name = 'Snow'
    disponibility = [{'Martes': '9.00'}, {'Miércoles': '15.00'}]
    level = 'Intermediate'
    modality = 'Grupal'