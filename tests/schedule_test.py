import pytest

# Test Schedule model
@pytest.mark.django_db # Set up access to db
def test_schedule_creation(schedule_creation):
    print(schedule_creation.name) # print on console if I run this with 'pytest -rP' 
    schedule_creation.save()
    assert schedule_creation.day == 'Lunes' # test confirmation

@pytest.mark.django_db 
def test_schedule_creation_fail(schedule_creation):
    schedule_creation.save()
    with pytest.raises(Exception):
            schedule = schedule_creation(
                day = 'Lunes',
                hour = '9.00'
            ) # We are checking the exception be catch up
