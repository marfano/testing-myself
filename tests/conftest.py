import pytest

from .factories import StudentFactory, tEACHERfACTORY

@pytest.fixture
def student_creation():
    return StudentFactory.build() # build makes an only one instance


@pytest.fixture
def teacher_creation():
    return TeacherFactory.build() # build makes an only one instance