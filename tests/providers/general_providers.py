import random
from faker import Faker
from faker.providers import BaseProvider

fake = Faker()

class EmailProvider(BaseProvider):

    def custom_email(self):
        email = [f'{fake.last_name().lower()}@gmail.com' for i in range(3)]
        # This select a random email from the list and return it
        return random.choice(email)