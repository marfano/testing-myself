from django.db import models

# Create your models here.

class Schedule(models.Model):
    """Model definition for Schedule object"""

    # Days of week to choice
    Monday = 'M'
    Tuesday = 'TU'
    Wednesday = 'W'
    Thursday = 'TH'
    Friday = 'F'
    DAYS_OF_WEEK_CHOICES = [
        (Monday, 'Lunes'),
        (Tuesday, 'Tuesday'),
        (Wednesday, 'Wednesday'),
        (Thursday, 'Thursday'),
        (Friday, 'Friday'),
    ]

    # Hs of day to choice
    HS_OF_DAY_CHOICES = [(x, f'{x}.00') for x in range(9,20)]

    # The fields
    day = models.CharField(max_length=20, choices = DAYS_OF_WEEK_CHOICES, default = None) 
    hour = models.CharField(max_length=20, choices = HS_OF_DAY_CHOICES, default = None)

    class Meta:
        """Meta definition for Schedule"""
        db_table = 'Schedules'
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'
        ordering = ['day', '-hour'] # ordered by day and hour

    def ___str__(self):
        """"Unicode representation of Schedule"""
        text = "{0} {1}"
        return text.format(self.day, self.hour)