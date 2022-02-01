from django.db import models

from apps.schedule.models import Schedule
import apps.course.courses_settings as Settings


class Person(models.Model):
    """"Model definition for abstract class Person"""

    email = models.CharField('Email', max_length= 200, null = False, blank = False)
    name = models.CharField('Nombre', max_length= 200, blank = False, null = False)
    last_name = models.CharField('Apellido', max_length = 220, blank = False, null = False)
    disponibility = models.ManyToManyField(Schedule, null = True, blank = True)

    class Meta:        
        abstract = True

class Student(Person):
    """Model definition for Student - type of Person"""

    # Choices
    modality = models.CharField(max_length=20, choices = Settings.modalities, default = 'Grupal')
    level = models.CharField(max_length=20, choices = Settings.levels, default = 'Begginer') 
    
    class Meta:
        """Meta definition for Student"""
        db_table = 'students'
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ['name'] # alphabetic order

    def ___str__(self):
        """"Unicode representation of Student"""
        text = "{0} {1}"
        return text.format(self.name, self.last_name)


class Teacher(Person):
    """Model definition for Teacher"""
   
    class Meta:
        """Meta definition for Teacher"""
        db_table = 'teachers'
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
        ordering = ['name'] # alphabetic order

    def ___str__(self):
        """"Unicode representation of Teacher"""
        text = "{0} {1}"
        return text.format(self.name, self.last_name)