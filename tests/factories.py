import pytest
import factory

from apps.person.models import Student

class StudentFactory(factory.Factory):  
    class Meta:
        model = Student

    email = 'john.snow@stark.com'
    name = 'John'
    last_name = 'Snow'
    modality = 'Grupal'
    level = 'Intermediate'
   