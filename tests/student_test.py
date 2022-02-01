import pytest
from faker import Faker

fake = Faker()

# Test Student model 
@pytest.mark.django_db # Set up access to db
def test_student_creation(student_creation):
    """The student is created properly"""
    print(student_creation.name) # print on console if I run this with 'pytest -rP' 
    student_creation.save()
    assert '@gmail.com' in student_creation.email  # test confirmation

@pytest.mark.django_db 
def test_student_creation_fail(student_creation):
    student_creation.save()
    with pytest.raises(Exception):
            student = student_creation(
                name = fake.name(),
                last_name = fake.last_name()
            ) # We are checking the exception be catch up
            # This test pass
            # 
  
           