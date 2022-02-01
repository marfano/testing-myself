import pytest

from .factories import StudentFactory, TeacherFactory, ScheduleFactory

@pytest.fixture
def student_creation():
    return StudentFactory.build() 


@pytest.fixture
def teacher_creation():
    return TeacherFactory.build()

@pytest.fixture
def schedule_creation():
    return ScheduleFactory.build()