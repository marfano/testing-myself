import random
from faker import Faker
from faker.providers import BaseProvider

fake = Faker()

class HourProvider(BaseProvider):

    def list_hours(self):
        HS_OF_DAY_CHOICES = [(f'{x}.00') for x in range(9,20)]
        return HS_OF_DAY_CHOICES

    def custom_hour(self):
        # This select a random hour from the list and return it
        return random.choice(self.list_hours())


class DayProvider(BaseProvider):

    def list_days(self):
        DAYS_OF_WEEK_CHOICES = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
        return DAYS_OF_WEEK_CHOICES

    def custom_day(self):
        # This select a random week-day from the list and return it
        return random.choice(self.list_days())
