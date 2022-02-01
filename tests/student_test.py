import pytest

# Test Student model 
@pytest.mark.django_db # Set up access to db
def test_student_creation(student_creation):
    print(student_creation.name) # print on console if I run this with 'pytest -rP' 
    student_creation.save()
    assert student_creation.email == 'john.snow@stark.com' # test confirmation

@pytest.mark.django_db 
def test_student_creation_fail(student_creation):
    student_creation.save()
    with pytest.raises(Exception):
            student = student_creation(
                name = 'John',
                lastName = 'Snow'
            ) # We are checking the exception be catch up
            # This test pass
            # 
  
           