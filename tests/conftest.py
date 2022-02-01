import pytest

from .factories import StudentFactory, TeacherFactory

@pytest.fixture
def student_creation():
    return StudentFactory.build() 


@pytest.fixture
def teacher_creation():
    return TeacherFactory.build()