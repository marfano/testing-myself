import pytest
from faker import Faker

fake = Faker()

from .providers.schedule_providers import DayProvider, HourProvider
fake.add_provider(DayProvider)
fake.add_provider(HourProvider)

# Test Schedule model
@pytest.mark.django_db # Set up access to db
def test_schedule_creation(schedule_creation):
    """The schedule is created properly"""
    #print(schedule_creation.day) # print something like 'Viernes'
    schedule_creation.save()
    
    assert schedule_creation.day in fake.list_days() # test confirmation
    assert schedule_creation.hour in fake.list_hours()

@pytest.mark.django_db 
def test_schedule_creation_fail(schedule_creation):
    schedule_creation.save()
    with pytest.raises(Exception):
            schedule = schedule_creation(
                day = fake.custom_day(),
                hour = fake.custom_hour()
            ) # We are checking the exception be catch up

