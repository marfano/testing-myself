import pytest
from faker import Faker

fake = Faker()

# 2) Adding a teacher
@pytest.mark.django_db # Set up access to db
def test_teacher_creation(teacher_creation):
    print(teacher_creation.name) 
    teacher_creation.save()
    assert '@gmail.com' in teacher_creation.email # test confirmation


@pytest.mark.django_db 
def test_teacher_creation_fail(teacher_creation):
    teacher_creation.save()
    with pytest.raises(Exception):
            teacher = teacher_creation(
                name = fake.name(),
                lastName = fake.last_name()
            ) # We are checking the exception be catch up