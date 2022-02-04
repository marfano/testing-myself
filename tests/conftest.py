import pytest

from .factories import *

# This <test>.py doc works first

@pytest.fixture
def student_creation():
    return StudentFactory.build() 

@pytest.fixture
def teacher_creation():
    return TeacherFactory.build()

@pytest.fixture
def schedule_creation():
    return ScheduleFactory.build()

@pytest.fixture
def course_creation():
    return CourseFactory.create_course()

@pytest.fixture
def settings_creation():
    return settings_setup()
