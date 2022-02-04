import pytest
from faker import Faker

fake = Faker()

# 4) Adding a course
@pytest.mark.django_db # Set up access to db
def test_course_creation(course_creation):
    """The course is created properly"""
    # print(course_creation) # somethingh like -> Course object (1)
    course_creation.save()
    assert course_creation != None  # test confirmation
