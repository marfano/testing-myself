from django.db import models

from apps.person.models import Student, Teacher
from apps.schedule.models import Schedule

class Course(models.Model):
    """"Model definition for Course"""

    id = models.CharField(auto_created=True, max_length=10, primary_key=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student) 
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Course"""
        db_table = 'courses'
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['id'] # creation order

    def ___str__(self):
        """"Unicode representation of Course"""
        text = "Curso dictado por {0} {1} el {2} a las {3}hs"
        return text.format(self.teacher.name, self.teacher.name, self.schedule.day, self.schedule.hour)
