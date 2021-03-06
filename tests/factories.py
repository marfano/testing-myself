import pytest
from faker import Faker
import factory
from ddf import G, F

from apps.person.models import Student, Teacher
from apps.schedule.models import Schedule
from apps.course.models import Course
import apps.course.courses_settings as Settings

fake = Faker()

from .providers.general_providers import EmailProvider
from .providers.student_providers import ModalityProvider, LevelProvider
from .providers.schedule_providers import DayProvider, HourProvider

fake.add_provider(EmailProvider)
fake.add_provider(ModalityProvider)
fake.add_provider(LevelProvider)
fake.add_provider(DayProvider)
fake.add_provider(HourProvider)

class ScheduleFactory(factory.Factory):  
    class Meta:
        model = Schedule
    id = fake.random_digit()
    day = fake.custom_day()
    hour = fake.custom_hour()

class StudentFactory(factory.Factory):  
    class Meta:
        model = Student
    email = fake.custom_email()
    name = fake.name()
    last_name = fake.last_name()
    modality = fake.custom_modality() 
    level = fake.custom_level()


class TeacherFactory(factory.Factory):  
    class Meta:
        model = Teacher
    email = fake.custom_email()
    name = fake.name()
    last_name = fake.last_name()


class CourseFactory(factory.Factory):  
    class Meta:
        model = Course
    def create_course():
        return G(Course, teacher=F(), schedule=F(day=fake.custom_day(), hour=fake.custom_hour())) 

def settings_setup():  
    return Settings