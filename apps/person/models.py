from django.db import models

# Create your models here.


class Person(models.Model):
    """"Model definition for abstract class Person"""

    email = models.CharField('Email', max_length= 200, null = False, blank = False)
    name = models.CharField('Nombre', max_length= 200, blank = False, null = False)
    last_name = models.CharField('Apellido', max_length = 220, blank = False, null = False)
    # disponibility = models.ManyToManyField('Horarios') # Many to Many to DateTime

    class Meta:        
        abstract = True

class Student(Person):
    """Model definition for Student - type of Person"""

    # Levels to choice
    begginer = 'B'
    pre_intermediate = 'PI'
    intermediate = 'I'
    upper_intermediate = 'UI'
    advanced = 'A'
    LEVEL_CHOICES = [
        (begginer, 'Begginer'),
        (pre_intermediate, 'Pre_Intermediate'),
        (intermediate, 'Intermediate'),
        (upper_intermediate, 'Upper-intermediate'),
        (advanced, 'Advanced'),
    ]

    # Modalities to choice
    individual = 'I'
    grupal = 'G'
    MODALITY_CHOICES = [
        (individual, 'Individual'),
        (grupal, 'Grupal'),
    ]

    # Choices
    modality = models.CharField(max_length=20, choices = MODALITY_CHOICES, default = grupal)
    level = models.CharField(max_length=20, choices = LEVEL_CHOICES, default = begginer) 

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