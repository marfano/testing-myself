import pytest
from faker import Faker

fake = Faker()

from .providers.student_providers import ModalityProvider, LevelProvider
from .providers.schedule_providers import DayProvider

fake.add_provider(ModalityProvider)
fake.add_provider(LevelProvider)
fake.add_provider(DayProvider)

# Adding a settings instance
def test_settings_creation(settings_creation):
    """The settings is created properly"""
    
    # print(settings_creation.min_hour) # print something like '9'

    ## Test confirmations
    assert ('Lunes', 'Lunes') in settings_creation.days_of_week  

    assert type(settings_creation.min_hour) is int
    assert type(settings_creation.max_hour) is int

    assert ('Intermediate', 'Intermediate') in settings_creation.levels    
    assert ('Individual', 'Individual') in settings_creation.modalities
    
    assert type(settings_creation.journey()) == list