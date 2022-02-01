import pytest

from .factories import StudentFactory

@pytest.fixture
def student_creation():
    return StudentFactory.build() # build makes an only one instance
