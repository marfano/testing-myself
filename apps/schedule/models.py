from django.db import models
import apps.course.courses_settings as Settings

# Create your models here.

class Schedule(models.Model):
    """Model definition for Schedule object"""

    # The fields
    day = models.CharField(max_length=20, choices = Settings.days_of_week, default = None) 
    hour = models.CharField(max_length=20, choices = Settings.journey(), default = None)

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
        