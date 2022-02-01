import random
from faker import Faker
from faker.providers import BaseProvider

fake = Faker()

class ModalityProvider(BaseProvider):

    def custom_modality(self):
        modality = ['Grupal', 'Individual']
        # This select a random modality from the list and return it
        return random.choice(modality)


class LevelProvider(BaseProvider):

    def custom_level(self):
        level = ['Begginer', 'Pre-Intermediate', 'Intermediate', 'Upper-Intermediate', 'Advanced']
        # This select a random level from the list and return it
        return random.choice(level) 