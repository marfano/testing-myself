import pytest

from apps.person.models import Teacher

# Test Teacher model
@pytest.mark.django_db # Set up access to db
def test_teacher_creation(teacher_creation):
    print(teacher_creation.name) 
    teacher_creation.save()
    assert teacher_creation.email == 'master.yoda@gimmerstick.com' # test confirmation


@pytest.mark.django_db 
def test_teacher_creation_fail(teacher_creation):
    teacher_creation.save()
    with pytest.raises(Exception):
            teacher = teacher_creation(
                name = 'Master',
                lastName = 'Yoda'
            ) # We are checking the exception be catch up
