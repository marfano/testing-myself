import pytest
from faker import Faker

fake = Faker()

from .providers.student_providers import ModalityProvider, LevelProvider
from .providers.schedule_providers import DayProvider, HourProvider

fake.add_provider(ModalityProvider)
fake.add_provider(LevelProvider)
fake.add_provider(DayProvider)
fake.add_provider(HourProvider)

# 5) Adding a settings instance
@pytest.mark.django_db # Set up access to db
def test_settings_creation(settings_creation):
    """The settings is created properly"""

    # tolerancia de inscriptos
    # max_inscriptos
    # margen de días
    # margen de horas
    # niveles
    # modalidades

    # print(settings_creation.day) 
    settings_creation.save()

    ## Test confirmations
    assert settings_creation.min_day in fake.list_days()
    assert settings_creation.max_day in fake.list_days()

    assert settings_creation.min_hour in fake.list_hours()
    assert settings_creation.max_hour in fake.list_hours()

    assert type(settings_creation.tolerance) is int
    assert settings_creation.levels in fake.list_levels()

    assert settings_creation.modalities in fake.list_days()
    assert type(settings_creation.capacity) is int