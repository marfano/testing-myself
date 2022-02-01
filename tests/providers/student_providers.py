import random
from faker import Faker
from faker.providers import BaseProvider

fake = Faker()

class ModalityProvider(BaseProvider):

    def list_modalities(self):
        modalities = ['Grupal', 'Individual']
        return modalities

    def custom_modality(self):
        # This select a random modality from the list and return it
        return random.choice(self.list_modalities())


class LevelProvider(BaseProvider):

    def list_levels(self):
        levels = ['Begginer', 'Pre-Intermediate', 'Intermediate', 'Upper-Intermediate', 'Advanced']
        return levels

    def custom_level(self):
        # This select a random level from the list and return it
        return random.choice(self.list_levels())