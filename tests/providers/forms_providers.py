from faker import Faker
from faker.providers import BaseProvider

from .general_providers import EmailProvider
from .student_providers import LevelProvider, ModalityProvider
from .schedule_providers import DayProvider, HourProvider

fake = Faker()

fake.add_provider(EmailProvider)
fake.add_provider(LevelProvider)
fake.add_provider(ModalityProvider)
fake.add_provider(DayProvider)
fake.add_provider(HourProvider)

class FormStudentProvider(BaseProvider):

    def form_data(self):
        form_data = {
            'email': fake.custom_email(),
            'name': fake.name(),
            'last_name': fake.last_name(),
            'modality': fake.custom_modality(),
            'level': fake.custom_level(),
            'disponibility': [ ],}
        return form_data